# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views for students
def students_list(request):
	students = (
        {'id': 1,
         'first_name': u'Адріан',
         'last_name': u'Яворський􏰁􏰀􏰁􏰓􏰂',
         'ticket': 12345,
         'image': 'img/me.jpg'},
         {'id': 2,
         'first_name': u'Роман',
         'last_name': u'Боровець􏰁􏰀􏰁􏰓􏰂',
         'ticket': 12346,
         'image': 'img/Roma.jpg'},
         {'id': 3,
         'first_name': u'Назар',
         'last_name': u'Мельничук􏰁􏰀􏰁􏰓􏰂',
         'ticket': 12347,
         'image': 'img/Nazar.jpg'},
        
	)
	return render(request, 'students/students_list.html',
		{'students': students})

def students_add(request):
    return HttpResponse('<h1> Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1> Edit student %s </h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1> Delete student %s </h1>' % sid)