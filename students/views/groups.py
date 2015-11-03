# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..models import Group
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

class GroupList(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'students/groups_list.html'

    def get_context_data(self, **kwargs):

        # groups = Group.objects.all()
        context = super(GroupList, self).get_context_data(**kwargs)

        context = paginate(self.object_list, 4, self.request, {}, var_name='groups')

        return context

    def get_queryset(self):
        groups = Group.objects.all()

        order_by = self.request.GET.get('order_by','')
        if order_by == '':
            self.request.GET.order_by = 'title'
            groups = groups.order_by('title')
        if order_by in ('leader','title', 'id'):
            groups=groups.order_by(order_by)
            if self.request.GET.get('reverse','') =='1':
                groups=groups.reverse()

        return groups


class GroupForm(ModelForm):
    class Meta:
        model=Group
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        #set form tag attributes
        if add_form:
            self.helper.form_action = reverse('groups_add')
        else:
            self.helper.form_action = reverse('groups_edit', kwargs={'pk':kwargs['instance'].id})

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'


        break_message= u"Додавання групи відмінено"
        #  set form field properties

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        if add_form:
            submit = Submit('add_button', u'Додати',css_class="btn btn-primary")
            self.helper.layout[-1]= Layout(
                Field('notes',css_class='input-xlarge',),
                FormActions(submit,
            HTML("<a class='btn btn-link' id = 'cancel-id-send_button' href='{% url 'groups_list' %}?status_message="+break_message+"' name = 'cancel_button'>"+u'Скасувати'+"</a>"),
            ))
        else:
            submit = Submit('save_button', u'Зберегти',css_class="btn btn-primary")
            cancel = Submit('cancel_button', u'Відмінити',css_class="btn btn-link")
            self.helper.layout[-1] = Layout(Field('notes',css_class='input-xlarge',),
            FormActions(submit, cancel))

class BaseGroupFormView(object):

    def get_success_url(self):
        return u'%s?status_message=Зміни успішно збережені!'%reverse ('groups_list')

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!'%reverse('groups_list'))
        else:
            return super(BaseGroupFormView, self).post(request, *args, **kwargs)


class GroupAddView(BaseGroupFormView, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/groups_universal.html'

    def get_context_data(self, **kwargs):

        context = super(GroupAddView, self).get_context_data(**kwargs)
        context['name'] = 'Додати'

        return context


class GroupUpdateView(BaseGroupFormView, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/groups_universal.html'



    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['name'] = 'Редагувати'

        return context

    # def post(self, request, *args, **kwargs):
    #     # import pdb; pdb.set_trace()
    #     if request.POST.get('cancel_button'):
    #         return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!'%reverse('groups_list'))
    #     else:
    #         return super(BaseGroupFormView, self).post(request, *args, **kwargs)
        

class GroupDeleteView(BaseGroupFormView, DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace();
        grouptodelete = self.get_object().title
        if request.POST.get('delete_button'): 
            try:
                return super(GroupDeleteView, self).post(request, *args, **kwargs)
            except ProtectedError:
                return  HttpResponseRedirect(reverse('groups_list') + u'?status_message=Зміни не можуть бути збережені, оскільки  є ще студенти в ' 
                     + grouptodelete)
        else:
            return HttpResponseRedirect(u'%s?status_message=Видалення групи відмінено!'%reverse('groups_list'))






        



# def groups_add(request):
# 	return HttpResponse('<h1> group add form</h1>')

# def groups_edit(request, gid):
# 	return HttpResponse('<h1> Edit Groups %s </h1>' %gid)

# def groups_delete(request, gid):
# 	return HttpResponse('<h1> Delete Groups %s </h1>' %gid)