# Generated by Django 3.0 on 2020-04-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0005_barang_stok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='harga',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='barang',
            name='stok',
            field=models.CharField(choices=[('1', 'Stok Ada'), ('2', 'Stok Kosong'), ('3', 'Stok Sedikit')], default='Stok Ada', max_length=13),
        ),
    ]
