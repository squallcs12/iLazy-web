# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150417_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='responses',
            field=models.TextField(default=''),
        ),
    ]
