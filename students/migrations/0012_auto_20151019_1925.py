# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20151019_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_teacher',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87', blank=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
