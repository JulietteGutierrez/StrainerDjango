# Generated by Django 3.2.18 on 2023-05-31 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]