# Generated by Django 3.0 on 2020-04-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0011_auto_20200426_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesan',
            name='warna',
            field=models.CharField(choices=[('1', 'Elegant Brown'), ('2', 'Black Coil'), ('3', 'Combination')], default='Elegant Brown', max_length=20),
        ),
    ]
