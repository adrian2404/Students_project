# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150302_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, blank=True, to='students.Student', verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
    ]
