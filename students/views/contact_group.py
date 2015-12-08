# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages
from django.contrib.messages import get_messages


from studentsdb.settings import ADMIN_EMAIL

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.views.generic.edit import FormView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.models import AbstractUser, User


class ContactForm(forms.Form):

	def __init__(self, *args, **kwargs):
		#call original initializator
		super(ContactForm, self).__init__(*args, **kwargs)

		import pdb; pdb.set_trace;
		#this helper object allows us to customize form 
		self.helper = FormHelper()

		# form tag attributes
		self.helper.form_class = 'form-horizontal'
		self.helper.form_mehtod = 'post'
		self.helper.form_action = reverse('contact_group')

		#twitter bootstrap styles

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		#form buttons 
		self.helper.add_input(Submit('send_button',u'Надіслати'))
	
	from .groups import Group
	group = forms.ModelChoiceField(queryset = Group.objects.all(), empty_label="Обрати групу",label=u"Група")

	subject = forms.CharField(label=u"Заголовок листа", max_length = 128)

	message = forms.CharField(label=u"Текст повідомлення", max_length=2560, widget = forms.Textarea)


class ContactGroup(FormView):
	
	template_name="students/contact_form.html"
	form_class = ContactForm

	def get_context_data(self, *args, **kwargs):

	    context = super(ContactGroup, self).get_context_data(*args, **kwargs)
	    context["name"] = "Групою"

	    return context
	# success_message="Повідомлення успішно відправлено."
#	success_url=reverse_lazy('contact_admin')
       
	def get_success_url(self):
    	    return reverse('contact_group')

	def form_valid(self,form):
	    # import pdb; pdb.set_trace();
	    # if leader has no email attached
	    try:
	    	group = form.cleaned_data['group']
	    	group_email = group.leader.user.email
	    except:
	    	return HttpResponseRedirect(u'%s?status_message=Помилка на сервері'%reverse('contact_group'))
	    
	    subject = form.cleaned_data['subject']
    	    message = form.cleaned_data['message']
    	    

    	    send_mail(subject, message, 'Student DB', [group_email])
    	    # email_user(subject, message)
    	    storage = get_messages(self.request)
    	    for message in storage:
        	pass
    	    messages.add_message(self.request, messages.INFO, "Повідомлення успішно відправлено.")
    	    return super(ContactGroup, self).form_valid(form)

	

