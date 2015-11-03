# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20151019_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('subject', models.CharField(max_length=256, null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447',
                'verbose_name_plural': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456',
            },
            bases=(models.Model,),
        ),
    ]
