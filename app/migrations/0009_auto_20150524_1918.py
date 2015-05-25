# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_handheldcambioestado_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handheldcambioestado',
            name='observacion',
            field=models.TextField(blank=True),
        ),
    ]
