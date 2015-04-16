# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_app_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='app',
            name='price_life',
            field=models.DecimalField(default=10.0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='app',
            name='request_sites',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='app',
            name='require_params',
            field=models.TextField(default=''),
        ),
    ]
