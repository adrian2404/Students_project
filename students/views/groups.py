# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'КН-30',
         'leader': {'id': 1, 'name': u'Адріан Яворський'}},
        {'id': 2,
         'name': u'КН-31',
         'leader': {'id': 2, 'name': u'Роман Боровець'}},
         {'id': 3,
         'name': u'КН-32',
         'leader': {'id': 3, 'name': u'Назар Мельничук'}},
    )
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1> group add form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1> Edit Groups %s </h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1> Delete Groups %s </h1>' %gid)