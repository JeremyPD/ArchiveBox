# Generated by Django 5.0.6 on 2024-08-20 03:30

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_rename_id_tag_old_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='old_id',
            field=models.BigIntegerField(default=core.models.rand_int_id, primary_key=True, serialize=False, verbose_name='Old ID'),
        ),
    ]
