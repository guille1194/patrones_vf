# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0007_pregunta_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='image',
        ),
    ]
