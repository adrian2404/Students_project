# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..models import Exam
from ..util import paginate, get_current_group

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.db.models.deletion import ProtectedError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Field
# Create your views here.
# Views for exams

class ExamList(ListView):
	model = Exam
	context_object_name = 'exams'
	template_name = 'students/exams_list.html'

	def get_context_data(self, **kwargs):

		context = super(ExamList, self).get_context_data(**kwargs)

		context = paginate(self.object_list, 4, self.request, {}, var_name = 'exams')

		return context

	def get_queryset(self):
		current_group = get_current_group(self.request)
		if current_group:
			exams = Exam.objects.filter(groups=current_group)
		else:
		  exams = Exam.objects.all()
		# import pdb; pdb.set_trace();
		order_by = self.request.GET.get('order_by', '')
		if (order_by == ''):
			self.request.GET.order_by = 'name'	
		if(order_by in ('name', 'exam_teacher', 'id', 'date')):
			exams = exams.order_by(order_by)
			if self.request.GET.get('reverse','') == '1':
				exams = exams.reverse()

		else:
			exams = exams.order_by('name')

		return exams

class ExamForm(ModelForm):
	class Meta:
		model=Exam
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(ExamForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		if kwargs['instance'] is None:
			add_form = True
		else:
			add_form = False

		#set form tag attributes
		if add_form:
			self.helper.form_action = reverse('exams_add')
		else:
			self.helper.form_action = reverse('exams_edit', kwargs={'pk':kwargs['instance'].id})

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		break_message= u"Додавання  екзамену відмінено"
		#  set form field properties

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		if add_form:
			submit = Submit('add_button', u'Додати',css_class="btn btn-primary")
			self.helper.layout[-1]= Layout(
				Field('notes',css_class='input-xlarge',),
				FormActions(
			Submit('add_button',u'Зберегти', css_class="btn btn-priamry"),
			HTML("<a class='btn btn-link' id = 'cancel-id-send_button' href='{% url 'exams_list' %}?status_message="+break_message+"' name = 'cancel_button'>"+u'Скасувати'+"</a>"),
			))
		else:
			submit = Submit('save_button', u'Зберегти',css_class="btn btn-primary")
			cancel = Submit('cancel_button', u'Відмінити',css_class="btn btn-link")
			self.helper.layout[-1] = Layout(Field('notes',css_class='input-xlarge',),
			FormActions(submit, cancel))

class BaseExamFormView(object):

	def get_success_url(self):
		return u'%s?status_message=Зміни успішно збережені'%reverse('exams_list')

	def post (self, request, *args, **kwargs):
		if request.GET.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Зміни скасовано'%reverse('exams_list'))
		else:
			return super(BaseExamFormView, self).post(request,*args, **kwargs)

class ExamAddView(BaseExamFormView, CreateView):
	model = Exam
	template_name = 'students/exams_universal.html'
	form_class = ExamForm

	def get_context_data(self, **kwargs):

		context = super(ExamAddView, self).get_context_data(**kwargs)
		context['name'] = 'Додати'

		return context


class ExamEditView(BaseExamFormView, UpdateView):
	model = Exam
	template_name = 'students/exams_universal.html'
	form_class = ExamForm

	def get_context_data(self, **kwargs):
		context = super(ExamEditView, self).get_context_data(**kwargs)
		context['name'] = 'Редагувати'

		return context

class ExamDeleteView(BaseExamFormView, DeleteView):
	model = Exam
	template_name = 'students/exams_confirm_delete.html'

	def post (self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Видалення екзамену скасовано'%reverse('exams_list'))
		else:
			return super(ExamDeleteView, self).post(request,*args, **kwargs)

