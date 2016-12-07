# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='opciones',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=64)),
                ('seleccionar', models.BooleanField(default=False)),
                ('terminar', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('id_usuario', models.ForeignKey(to='voto.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta_opcion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('id_opciones', models.ManyToManyField(to='voto.opciones')),
                ('id_pregunta', models.ForeignKey(to='voto.pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='opciones',
            name='id_pregunta',
            field=models.ForeignKey(to='voto.pregunta'),
        ),
    ]
