# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20160112_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='sar',
            new_name='identificator',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='turnover_code',
            new_name='implementationId',
        ),
        migrations.RenameField(
            model_name='taskcomment',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 28, 57, 747192, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 7, 27380, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 11, 451518, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 17, 875502, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 24, 291448, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 29, 611540, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 34, 59408, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 39, 3587, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 43, 851423, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 48, 443536, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 29, 54, 707624, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 0, 515570, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 10, 219503, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 17, 3225, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urgency',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 22, 475521, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urgency',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 30, 451188, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 34, 27490, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 39, 699348, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 41, 523578, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 15, 30, 42, 731274, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
