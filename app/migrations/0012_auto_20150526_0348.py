# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150526_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centrodistribucion',
            name='nombre',
        ),
        migrations.AddField(
            model_name='centrodistribucion',
            name='codigo',
            field=models.CharField(unique=True, default=1, max_length=4, validators=[django.core.validators.RegexValidator('[0-9]{4}$', 'Codigo debe ser 4 numeros.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centrodistribucion',
            name='sucursal',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='legajo',
            field=models.CharField(unique=True, max_length=8, validators=[django.core.validators.RegexValidator('^[0-9]{8}$', 'Legajo debe ser 8 numeros.')]),
        ),
    ]
