# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_result_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='app',
            name='price_life',
            field=models.IntegerField(),
        ),
    ]
