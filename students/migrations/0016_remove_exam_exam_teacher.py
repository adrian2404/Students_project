# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20151105_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_teacher',
        ),
    ]
