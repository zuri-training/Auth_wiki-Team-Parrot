# Generated by Django 4.1.4 on 2022-12-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(default='male.png', max_length=100),
        ),
    ]
