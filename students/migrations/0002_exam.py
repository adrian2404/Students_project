# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('teacher', models.CharField(max_length=256, null=True, blank=True)),
                ('groups', models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', blank=True, to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
            bases=(models.Model,),
        ),
    ]
