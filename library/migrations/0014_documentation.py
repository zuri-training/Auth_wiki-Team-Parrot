# Generated by Django 4.1.4 on 2022-12-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_remove_likes_user_alter_post_dislikes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
