# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20160105_1059'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userclient',
            unique_together=set([('user', 'userR')]),
        ),
    ]
