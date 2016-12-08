# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0005_auto_20161208_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='image',
            field=models.ImageField(null=True, upload_to=b'Perfiles/', blank=True),
        ),
    ]
