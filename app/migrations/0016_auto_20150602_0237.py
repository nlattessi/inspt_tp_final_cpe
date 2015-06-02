# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20150601_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='fecha_carga',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
