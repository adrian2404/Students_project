# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Exam, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# Views for students
def exams_list(request):
	exams = Exam.objects.all()
	
   # ordering exams 
	order_by=request.GET.get('order_by','')
	exams=exams.order_by('name')
	if request.GET.get('order_by', '') == '':
	    request.GET.order_by = 'name'
	#order_by = request.GET.get('order_by', '')
    
	if order_by in ('name','teacher','groups','id'):
	    exams=exams.order_by(order_by)
	    if request.GET.get('reverse','')=='1':
        	exams=exams.reverse()
    
    #paginate exams
	paginator = Paginator(exams, 3)
	page = request.GET.get('page')
	try:
	    exams = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    exams = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    exams = paginator.page(paginator.num_pages)


	return render(request, 'students/exams_list.html',
		{'exams':exams})

def exams_add(request):
    return HttpResponse('<h1> Exam add form</h1>')

def exams_edit(request, exid):
    return HttpResponse('<h1> Edit Exam  %s </h1>' % exid)

def exams_delete(request, exid):
    return HttpResponse('<h1> Delete Exam %s </h1>' % exid)