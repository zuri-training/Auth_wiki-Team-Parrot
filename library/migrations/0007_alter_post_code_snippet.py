# Generated by Django 4.1.4 on 2022-12-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_rename_downloadnumber_post_numberofdownloads_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='code_snippet',
            field=models.TextField(),
        ),
    ]
