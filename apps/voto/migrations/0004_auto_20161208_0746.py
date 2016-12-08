# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0003_contestar_pregunta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestar_pregunta',
            name='id_opcion',
        ),
        migrations.AddField(
            model_name='contestar_pregunta',
            name='id_opcion',
            field=models.ManyToManyField(to='voto.opciones'),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='opcion',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
