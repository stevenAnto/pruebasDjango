# Generated by Django 4.0.6 on 2022-07-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
