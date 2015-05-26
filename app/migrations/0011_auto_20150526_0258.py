# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150525_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handheld',
            name='numero_de_serie',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]{11}$', 'Numero de serie debe de ser 11 caracteres alfanumericos.')], unique=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='legajo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Legajo debe ser 8 numeros.')], unique=True, max_length=8),
        ),
    ]
