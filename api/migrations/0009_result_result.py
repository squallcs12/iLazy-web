# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150416_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.TextField(default=''),
        ),
    ]
