# Generated by Django 5.0.4 on 2024-04-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]