# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..models import Teacher, Exam
from ..util import paginate

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.db.models.deletion import ProtectedError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Field

# def groups_list(request):
#     groups = Group.objects.all()


#     #ordering groups
#     order_by = request.GET.get('order_by','')
#     groups=groups.order_by('title')
#     if request.GET.get('order_by','') == '':
#         request.GET.order_by = 'title'

#     if order_by in ('leader', 'id','title'):
#         groups=groups.order_by(order_by)
#         if request.GET.get('reverse','')=='1':
#             groups = groups.reverse()

	#pagination

	# paginator = Paginator(groups, 3) # 

	# page = request.GET.get('page')
	# try:
	#     groups = paginator.page(page)
	# except PageNotAnInteger:
	#     # If page is not an integer, deliver first page.
	#     groups = paginator.page(1)
	# except EmptyPage:
	#     # If page is out of range (e.g. 9999), deliver last page of results.
	#     groups = paginator.page(paginator.num_pages)

	# context = paginate(groups, 4, request, {}, var_name='groups')


	# return render(request, 'students/groups_list.html',
	#     context)

class TeacherList(ListView):
	model = Teacher
	context_object_name = 'teachers'
	template_name = 'students/teachers_list.html'

	def get_context_data(self, **kwargs):
		context = super(TeacherList, self).get_context_data(**kwargs)

		# exams = Exam.objects.filter()
		
		
		context = paginate(self.object_list, 4, self.request, {}, var_name='teachers')
		context['exams'] = Exam.objects.all()
		# import pdb; pdb.set_trace();
		return context

	def get_queryset(self):
		teachers = Teacher.objects.all()

		order_by = self.request.GET.get('order_by','')
		if order_by == '':
			self.request.GET.order_by = 'last_name'
			teachers = teachers.order_by('last_name')
		if order_by in ('first_name','last_name','subject', 'id'):
			teachers=teachers.order_by(order_by)
			if self.request.GET.get('reverse','') =='1':
				teachers=teachers.reverse()

		return teachers


class TeacherForm(ModelForm):
	class Meta:
		model=Teacher
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(TeacherForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		if kwargs['instance'] is None:
			add_form = True
		else:
			add_form = False

		#set form tag attributes
		if add_form:
			self.helper.form_action = reverse('teachers_add')
		else:
			self.helper.form_action = reverse('teachers_edit', kwargs={'pk':kwargs['instance'].id})

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'


		break_message= u"Додавання викладача відмінено"
		#  set form field properties

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		if add_form:
			submit = Submit('add_button', u'Додати',css_class="btn btn-primary")
			self.helper.layout[-1]= Layout(

                FormActions(submit,
            HTML("<a class='btn btn-link' id = 'cancel-id-send_button' href='{% url 'teachers_list' %}?status_message="+break_message+"' name = 'cancel_button'>"+u'Скасувати'+"</a>"),
            ))
		else:
			submit = Submit('save_button', u'Зберегти',css_class="btn btn-primary")
			cancel = Submit('cancel_button', u'Відмінити',css_class="btn btn-link")
			self.helper.layout[-1] = Layout(Field('subject',css_class='input-xlarge',),
			FormActions(submit, cancel))

class BaseTeacherFormView(object):

	def get_success_url(self):
		return u'%s?status_message=Зміни успішно збережені!'%reverse ('teachers_list')

	def post(self, request, *args, **kwargs):
		# import pdb; pdb.set_trace()
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Редагування викладача відмінено!'%reverse('teachers_list'))
		else:
			return super(BaseTeacherFormView, self).post(request, *args, **kwargs)


class TeacherAddView(BaseTeacherFormView, CreateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'students/teachers_universal.html'

	def get_context_data(self, **kwargs):

		context = super(TeacherAddView, self).get_context_data(**kwargs)
		context['name'] = 'Додати'


		return context


class TeacherUpdateView(BaseTeacherFormView, UpdateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'students/teachers_universal.html'



	def get_context_data(self, **kwargs):
		context = super(TeacherUpdateView, self).get_context_data(**kwargs)
		context['name'] = 'Редагувати'

		return context

	# def post(self, request, *args, **kwargs):
	#     # import pdb; pdb.set_trace()
	#     if request.POST.get('cancel_button'):
	#         return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!'%reverse('groups_list'))
	#     else:
	#         return super(BaseGroupFormView, self).post(request, *args, **kwargs)
		

class TeacherDeleteView(BaseTeacherFormView, DeleteView):
    model = Teacher
    template_name = 'students/teachers_confirm_delete.html'

    def post (self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Видалення викладача скасовано'%reverse('teachers_list'))
        else:
            return super(ExamDeleteView, self).post(request,*args, **kwargs)

		



# def groups_add(request):
# 	return HttpResponse('<h1> group add form</h1>')

# def groups_edit(request, gid):
# 	return HttpResponse('<h1> Edit Groups %s </h1>' %gid)

# def groups_delete(request, gid):
# 	return HttpResponse('<h1> Delete Groups %s </h1>' %gid)