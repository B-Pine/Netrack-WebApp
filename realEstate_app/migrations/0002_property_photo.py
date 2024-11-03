# Generated by Django 5.1.2 on 2024-10-31 09:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
