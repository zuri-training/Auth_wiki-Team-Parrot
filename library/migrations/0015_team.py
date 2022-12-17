# Generated by Django 4.1.4 on 2022-12-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_documentation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('image_choice', models.CharField(choices=[('male.png', 'MALE'), ('female.jpg', 'FEMALE')], default='Select Gender', max_length=30)),
            ],
        ),
    ]