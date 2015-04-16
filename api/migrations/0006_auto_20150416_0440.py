# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_userapp_app'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='description',
            new_name='introduction',
        ),
    ]
