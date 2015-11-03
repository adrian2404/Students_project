# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_exam_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442', to='students.Exam', max_length=256, null=True),
            preserve_default=True,
        ),
    ]
