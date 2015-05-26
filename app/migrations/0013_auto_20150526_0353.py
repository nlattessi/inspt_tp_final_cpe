# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150526_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalidadVendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='vendedor',
            name='modalidad',
            field=models.ForeignKey(default=1, to='app.ModalidadVendedor', related_name='modalidad'),
            preserve_default=False,
        ),
    ]
