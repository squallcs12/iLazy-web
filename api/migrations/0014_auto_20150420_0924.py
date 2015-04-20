# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_usercoinshistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercoinshistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 20, 9, 24, 14, 377175, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercoinshistory',
            name='kind',
            field=models.IntegerField(choices=[(1, 'Buy App')]),
        ),
    ]
