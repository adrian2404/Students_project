# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='groups',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]
