# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0022_auto_20151125_1328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447', 'verbose_name_plural': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456', 'permissions': (('contact_student', 'Teacher can contact student'),)},
        ),
    ]
