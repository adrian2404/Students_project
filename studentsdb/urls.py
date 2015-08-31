from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG

from students.views.students import StudentUpdateView, StudentCreateView, StudentDeleteView
from students.views.contact_admin import ContactView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'students.views.students.students_list', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Student urls
    url(r'^students/add/$', StudentCreateView.as_view(),name='students_add'),

    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(),name='students_edit'),

    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete',name='students_delete'),
    url(r'^students/delete_several/$','students.views.students.students_delete_several',name='students_delete_several'),

    url(r'^admin/', include(admin.site.urls)),

    #Group urls
    url(r'^groups/$', 'students.views.groups.groups_list',name='groups_list'),

    url(r'^groups/add/$', 'students.views.groups.groups_add',name='groups_add'),

    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit',name='groups_edit'),

    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete',name='groups_delete'),

    #Journal  urls
     url(r'^journal/$', 'students.views.journal.journal', name='journal'),
     
    #Exams urls
    url(r'^exams/$', 'students.views.exams.exams_list',name='exams_list'),

    url(r'^exams/add/$', 'students.views.exams.exams_add',name='exams_add'),

    url(r'^exams/(?P<exid>\d+)/edit/$', 'students.views.exams.exams_edit',name='exams_edit'),

    url(r'^exams/(?P<exid>\d+)/delete/$', 'students.views.exams.exams_delete',name='exams_delete'),

    #teachers urls
    url(r'^teachers/$', 'students.views.teachers.teachers_list', name='teachers_list'),

    url(r'^teachers/add/$', 'students.views.teachers.teachers_add',name='teachers_add'),

    url(r'^teachers/(?P<pk>\d+)/edit/$', 'students.views.teachers.teachers_edit',name='teachers_edit'),

    url(r'^teachers/(?P<sid>\d+)/delete/$', 'students.views.teachers.teachers_delete',name='teachers_delete'),
    
    #Contact Admin Form 
    url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),
    
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
# serve files from media folder 
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))