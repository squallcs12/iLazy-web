# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_app_responses'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapp',
            name='expires',
            field=models.DateField(null=True),
        ),
    ]
