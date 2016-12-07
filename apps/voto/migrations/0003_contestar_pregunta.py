# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0002_auto_20161207_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='contestar_pregunta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('id_opcion', models.ForeignKey(to='voto.opciones')),
                ('id_pregunta_opcion', models.ForeignKey(to='voto.pregunta_opcion')),
            ],
        ),
    ]
