# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_exam_exam_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
    ]
