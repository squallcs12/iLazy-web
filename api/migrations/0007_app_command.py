# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150416_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='command',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
