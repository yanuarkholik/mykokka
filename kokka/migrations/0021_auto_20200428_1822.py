# Generated by Django 3.0 on 2020-04-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0020_auto_20200428_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesan',
            name='kab',
        ),
        migrations.RemoveField(
            model_name='pesan',
            name='kel',
        ),
        migrations.RemoveField(
            model_name='pesan',
            name='prov',
        ),
        migrations.AlterField(
            model_name='pesan',
            name='alamat',
            field=models.TextField(),
        ),
    ]
