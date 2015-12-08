from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG

from students.views.students import StudentUpdateView, StudentCreateView, StudentDeleteView, StudentList
from students.views.groups import GroupList, GroupAddView, GroupUpdateView,GroupDeleteView 
from students.views.exams import ExamList, ExamAddView, ExamEditView, ExamDeleteView
from students.views.teachers import TeacherList, TeacherAddView, TeacherUpdateView, TeacherDeleteView
from students.views.contact_teacher import ContactTeacher
from students.views.contact_group import ContactGroup
from students.views.journal import JournalView
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # User Related urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'}, name='auth_logout'),

    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),name='registration_complete'),
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    # Examples:
    url(r'^$', StudentList.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Student urls
    url(r'^students/add/$', StudentCreateView.as_view(),name='students_add'),

    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(),name='students_edit'),

    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete',name='students_delete'),
    
    url(r'^students/delete_several/$','students.views.students.students_delete_several',name='students_delete_several'),

    url(r'^students/stats/$','students.views.stats.presense_stats',name='students_stats'),


    url(r'^admin/', include(admin.site.urls)),

    #Group urls
    url(r'^groups/$', GroupList.as_view(), name='groups_list'),

    url(r'^groups/add/$', login_required(GroupAddView.as_view()), name='groups_add'),

    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),

    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view() ,name='groups_delete'),

    #Journal  urls
     url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
     
    #Exams urls
    url(r'^exams/$', ExamList.as_view(), name='exams_list'),

    url(r'^exams/add/$', ExamAddView.as_view(),name='exams_add'),

    url(r'^exams/(?P<pk>\d+)/edit/$', ExamEditView.as_view(),name='exams_edit'),

    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view() ,name='exams_delete'),

    #teachers urls
    url(r'^teachers/$', TeacherList.as_view(), name='teachers_list'),

    url(r'^teachers/add/$', TeacherAddView.as_view() ,name='teachers_add'),

    url(r'^teachers/(?P<pk>\d+)/edit/$', TeacherUpdateView.as_view() ,name='teachers_edit'),

    url(r'^teachers/(?P<pk>\d+)/delete/$', TeacherDeleteView.as_view() ,name='teachers_delete'),
    
    #Contact Admin Form 
    url(r'^contact-teacher/$', ContactTeacher.as_view(), name='contact_teacher'),
    url(r'^contact-group/$', ContactGroup.as_view(), name='contact_group'),
    
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
# serve files from media folder 
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))