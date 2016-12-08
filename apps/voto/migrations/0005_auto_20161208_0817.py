# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0004_auto_20161208_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestar_pregunta',
            name='id_opcion',
        ),
        migrations.AddField(
            model_name='contestar_pregunta',
            name='id_opcion',
            field=models.ForeignKey(blank=True, to='voto.opciones', null=True),
        ),
    ]
