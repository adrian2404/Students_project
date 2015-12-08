# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0027_student_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438', 'permissions': (('contact_teacher', 'Student can contact teacher'), ('group_leader', 'Permission for managing the journal'))},
        ),
        migrations.AddField(
            model_name='teacher',
            name='notes',
            field=models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
