# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
#from django.view.generic import UpdateView
from django.forms import ModelForm
from django.views.generic import UpdateView

from ..models import Student, Group, Teacher

# Create your views here.
# Views for students
def teachers_list(request):
	teachers = Teacher.objects.all()
	
	# #ordering students 
	# order_by=request.GET.get('order_by','')
	# students=students.order_by('last_name')
	# if request.GET.get('order_by', '') == '':
	# 	request.GET.order_by = 'last_name'
	# #order_by = request.GET.get('order_by', '')
	
	# if order_by in ('last_name','first_name','ticket','id'):
	# 	students=students.order_by(order_by)
	# 	if request.GET.get('reverse','')=='1':
	# 		students=students.reverse()
	
	# #paginate students
	# paginator = Paginator(students, 3)
	# page = request.GET.get('page')
	# try:
	# 	students = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	students = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	# 	students = paginator.page(paginator.num_pages)


	return render(request, 'students/teachers_list.html',
		{'teachers': teachers})

def teachers_add(request):
    return HttpResponse('<h1> Teacher add  </h1>')
    # # If form was posted
    # if request.method == "POST":
    #     # was form add_button clicked
    #     if request.POST.get('add_button') is not None:

    #         data = {'middle_name':request.POST.get('middle_name'),'notes':request.POST.get('notes')}
    #         #TODO: validate input errors from user
    #         errors ={}

    #         first_name=request.POST.get('first_name','').strip()
    #         if not first_name:
    #             errors['first_name'] = u"Ім'я є обов'язковим"
    #         else:
    #             data['first_name']=first_name 

    #         last_name=request.POST.get('last_name','').strip()
    #         if not last_name:
    #             errors['last_name'] = u"Прізвище є обов'язковим"
    #         else:
    #             data['last_name']=last_name

    #         birthday=request.POST.get('birthday','').strip()
    #         if not birthday:
    #             errors['birthday'] = u"Дата народження є обов'язковою"
    #         else:
    #             try:
    #                 datetime.strptime(birthday,'%Y-%m-%d')
    #             except Exception:
    #                 errors['birthday']=u"Введіть коректну дату(напр. 1984-12-30)"

    #             else:
    #                 data['birthday']=birthday

    #         ticket=request.POST.get('ticket','').strip()
    #         if not ticket:
    #             errors['ticket'] = u"Номер білета є обов'язковим"
    #         else:
    #             data['ticket']=ticket

    #         student_group=request.POST.get('student_group','').strip()
    #         if not student_group:
    #             errors['student_group'] = u"Група є обов'язкова"
    #         else:
    #             groups=Group.objects.filter(pk=student_group)
    #             if len(groups)!=1:
    #                 errors['student_group']=u"Оберіть коректну групу"
    #             else:
    #                 data['student_group']=groups[0]

    #         formats = ['jpg','jpeg','bmp','png','gif','riff']

    #         photo=request.FILES.get('photo')
    #         if photo:
    #             file_name = photo.name.split('.')
    #             if photo.size > 2000000:
    #                 errors['photo'] = u"Розмір файлу завеликий"
    #             elif file_name[1] not in formats:
    #                 errors['photo'] = u"Це має бути фото"
    #             else:
    #                 data['photo']=photo

            

    #         if not errors:
    #             #create student
    #             student=Student(**data)
    #             #save student to database
    #             student.save()

    #             #redirect user to the students list

    #             return HttpResponseRedirect(u'%s?status_message=Студента успішно додано'%reverse('home'))

    #         else:
    #             # render form with errors and previous user input
    #             return render(request, 'students/students_add.html',{'groups':Group.objects.all().order_by('title'),
    #                 'errors':errors})
    #     elif request.POST.get('cancel_button') is not None:
    #         #redirect to homepage

    #         return HttpResponseRedirect(u'%s?status_message=Додавання студента відмінено'%reverse('home'))
    # else:
    #     #initial form render
    #     return render(request,'students/students_add.html',{'groups':Group.objects.all().order_by('title')})

    
# class StudentUpdateView(UpdateView):
#     model = Student
#     template_name = 'students/students_edit.html'
    

#     @property
#     def success_url(self):
#         return u'%s?status_message=Студента успішно збережено'%reverse('home')

#     def post(self,request, *args, **kwargs):
#         if request.POST.get('cancel_button'):
#             return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено'%reverse('home'))
#         else:
#             return super(StudentUpdateView, self).post(request,request, *args, **kwargs)


def teachers_edit(request,sid):
    return HttpResponse('<h1> Teacher edit %s </h1>' % sid)

def teachers_delete(request, sid):
	return HttpResponse('<h1> Delete teacher %s </h1>' % sid)