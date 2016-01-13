# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20160105_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 18, 57, 22, 477890, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
