# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160703_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
