# Generated by Django 3.2.7 on 2024-04-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20240417_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('UG', 'Підземна парковка'), ('SM', 'Багатоповерхова парковка'), ('SF', 'Не крита парковка')], max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер автостояночного місця'),
        ),
    ]