# Generated by Django 3.0 on 2020-04-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0014_auto_20200427_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='stok',
            field=models.CharField(choices=[('Stok Ada', 'Stok Ada'), ('Stok Kosong', 'Stok Kosong')], default='Stok Ada', max_length=13),
        ),
    ]