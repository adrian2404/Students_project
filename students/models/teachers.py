# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    """Group model"""

    class Meta(object):
        verbose_name=u"Викладач"
        verbose_name_plural= "Викладачі"
        permissions = (
            ("contact_student", "Teacher can contact student"),
        )



    first_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Ім'я")


    last_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Прізвище")


    middle_name = models.CharField(
    max_length=256,
    blank=True, 
    verbose_name=u"По-батькові",
    default='')


    birthday = models.DateField(
    blank=False,
    verbose_name=u"Дата народження",
    null=True)


    photo = models.ImageField(
    blank=True,
    verbose_name=u"Фото",
    null=True)

    notes = models.TextField(
    blank = True,
    verbose_name = u"Нотатки")

    user = models.OneToOneField(User,
    blank=True,
    null=True,
    verbose_name='Користувач')




    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)