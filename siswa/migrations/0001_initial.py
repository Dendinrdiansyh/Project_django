# Generated by Django 2.2.10 on 2021-09-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=100)),
                ('bidang_keahlian', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'siswa',
            },
        ),
    ]
