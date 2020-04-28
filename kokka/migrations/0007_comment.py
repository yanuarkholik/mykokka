# Generated by Django 3.0 on 2020-04-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokka', '0006_auto_20200426_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('waktu', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Data-Comment',
            },
        ),
    ]
