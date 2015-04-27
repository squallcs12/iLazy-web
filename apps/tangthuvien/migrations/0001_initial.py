# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('topic_id', models.PositiveIntegerField()),
                ('last_post_id', models.PositiveIntegerField()),
                ('last_post_number', models.PositiveIntegerField()),
                ('last_page_number', models.PositiveIntegerField()),
            ],
        ),
    ]
