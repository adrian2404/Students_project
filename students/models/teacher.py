# -*- coding: utf-8 -*-
from django.db import models

class Teacher(models.Model):
    """Group model"""

    class Meta(object):
        verbose_name=u"Викладач"
        verbose_name_plural= "Викладачі"



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

    

    subject = models.CharField(
    max_length=256,
    blank=False,
    null=True,
    verbose_name=u"Предмет")


    def __unicode__(self):
        return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)