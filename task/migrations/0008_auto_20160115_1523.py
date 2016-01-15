# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20160114_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notification',
            new_name='task',
        ),
    ]
