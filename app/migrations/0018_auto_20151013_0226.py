# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_incidente_revisado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidente',
            old_name='solucion',
            new_name='acciones',
        ),
    ]
