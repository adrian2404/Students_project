# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Student
from models import Group
from models import Exam

from django.forms import ModelForm, ValidationError
from django.core.urlresolvers import reverse
# Register your models here.
def make_copy(modelAdmin, request, queryset):
    
    for object in queryset:
        temp_obj = Student(first_name=object.first_name, last_name=object.last_name, middle_name= object.middle_name, birthday=object.birthday, ticket = object.ticket, notes = object.notes, student_group = object.student_group, photo = object.photo)
        temp_obj.save()
    make_copy.short_description =  "Скопіювати вибраних студентів"

class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group']!=groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи', code = "invalid")
        
        return self.cleaned_data['student_group']
        

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket','notes']
    actions = [make_copy]

    form = StudentFormAdmin
    
    def view_on_site(self, obj):
	return reverse('students_edit', kwargs={'pk':obj.id})
	
    
    

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Exam)
