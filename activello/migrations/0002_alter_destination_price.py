# Generated by Django 4.1.6 on 2023-02-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
