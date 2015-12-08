# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0026_teacher_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x87'),
            preserve_default=True,
        ),
    ]
