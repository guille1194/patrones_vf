# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0009_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='creado',
            field=models.DateField(default=django.utils.timezone.now, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_categoria',
            field=models.ForeignKey(blank=True, to='voto.categoria', null=True),
        ),
    ]
