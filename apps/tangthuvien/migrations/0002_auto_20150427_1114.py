# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangthuvien', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='last_page_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_post_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_post_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
