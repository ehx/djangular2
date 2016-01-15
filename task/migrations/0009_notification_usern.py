# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0008_auto_20160115_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='userN',
            field=models.ForeignKey(related_name='userN', default=0, verbose_name=b'Usuario que recibe notificacion', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
