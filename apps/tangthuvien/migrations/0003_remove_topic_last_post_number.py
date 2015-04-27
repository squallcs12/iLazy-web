# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangthuvien', '0002_auto_20150427_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='last_post_number',
        ),
    ]
