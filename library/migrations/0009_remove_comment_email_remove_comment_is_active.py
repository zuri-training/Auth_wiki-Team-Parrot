# Generated by Django 4.1.4 on 2022-12-14 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='is_active',
        ),
    ]
