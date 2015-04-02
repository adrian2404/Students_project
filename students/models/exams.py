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

    teacher = models.CharField(
    max_length=256,
    blank=False,
    null=True,
    verbose_name = "Викладач")

    groups = models.ForeignKey(
    'Group',
    blank=False,
    verbose_name='Група',
    null=True)

    def __unicode__(self):
        if self.teacher:
            return u"%s (%s)" % (self.name, self.teacher)
        else:
            return u"%s" % (self.name)