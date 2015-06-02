# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150526_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(validators=[django.core.validators.RegexValidator('[0-9]{4}$', 'El codigo debe ser 4 numeros.')], unique=True, max_length=4)),
                ('nombre', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='handheld',
            name='centro_distribucion',
        ),
        migrations.DeleteModel(
            name='CentroDistribucion',
        ),
        migrations.AddField(
            model_name='handheld',
            name='sucursal',
            field=models.ForeignKey(to='app.Sucursal', blank=True, null=True),
        ),
    ]
