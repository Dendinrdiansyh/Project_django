# Generated by Django 2.2.10 on 2021-09-13 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfileapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_avatar',
            new_name='bentuk_tugas',
        ),
    ]
