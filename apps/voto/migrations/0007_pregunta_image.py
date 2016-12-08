# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0006_usuario_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='image',
            field=models.ImageField(null=True, upload_to=b'Preguntas/', blank=True),
        ),
    ]
