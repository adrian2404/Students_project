from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'students.views.students.students_list', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Student urls
    url(r'^students/add/$', 'students.views.students.students_add',name='students_add'),

    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students.students_edit',name='students_edit'),

    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete',name='students_delete'),

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
    
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
# serve files from media folder 
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))