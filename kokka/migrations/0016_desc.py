# Generated by Django 3.0 on 2020-04-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0015_auto_20200427_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Buat-Barang-Desc',
            },
        ),
    ]
