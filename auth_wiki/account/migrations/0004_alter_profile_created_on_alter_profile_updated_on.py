# Generated by Django 4.1.4 on 2022-12-09 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_created_on_alter_profile_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]