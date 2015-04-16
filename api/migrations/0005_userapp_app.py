# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapp',
            name='app',
            field=models.ForeignKey(to='api.App', default=None),
            preserve_default=False,
        ),
    ]
