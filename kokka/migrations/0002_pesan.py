# Generated by Django 3.0 on 2020-04-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('hp', models.CharField(max_length=13)),
                ('kec', models.CharField(max_length=100)),
                ('kab', models.CharField(max_length=100)),
                ('prov', models.CharField(max_length=100)),
                ('neg', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Data-Pesan',
            },
        ),
    ]
