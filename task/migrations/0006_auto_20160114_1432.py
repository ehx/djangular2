# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20160114_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='implementationId',
            new_name='implementation_id',
        ),
    ]
