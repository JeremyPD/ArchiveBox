# Generated by Django 5.0.6 on 2024-08-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_alter_snapshot_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]
