# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20151019_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442'),
            preserve_default=True,
        ),
    ]
