# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Exam(models.Model):
    """Exam model"""

    class Meta(object):
        verbose_name=u"Екзамен"
        verbose_name_plural= "Екзамени" 


    name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Назва")

    date = models.DateTimeField(
    blank=False,
    verbose_name=u"Дата і час проведення",
    null=True)

    exam_teacher = models.ForeignKey('Teacher',
    max_length=256,
    blank=True,
    null=True,
    verbose_name = "Викладач")

    groups = models.ForeignKey(
    'Group',
    blank=False,
    verbose_name='Група',
    null=True)

    notes = models.TextField(
    blank=True,
    verbose_name=u"Нотатки")

    def __unicode__(self):
        if self.exam_teacher:
            return u"%s (%s %s)" % (self.name, self.exam_teacher.first_name, self.exam_teacher.last_name)
        else:
            return u"%s" % (self.name)