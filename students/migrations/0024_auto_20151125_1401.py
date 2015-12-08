# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20151125_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438', 'permissions': (('contact_teacher', 'Teacher can contact teacher'),)},
        ),
    ]
