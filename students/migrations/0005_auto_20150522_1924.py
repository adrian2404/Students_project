# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_exam'),
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
                ('subject', models.CharField(max_length=256, null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447',
                'verbose_name_plural': '\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='exam',
            name='teacher',
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_teacher',
            field=models.OneToOneField(null=True, to='students.Teacher', max_length=256, blank=True, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='groups',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', to='students.Group', null=True),
            preserve_default=True,
        ),
    ]
