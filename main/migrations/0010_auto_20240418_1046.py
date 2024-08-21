# Generated by Django 3.2.7 on 2024-04-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_parking_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('UG', 'Підземна парковка'), ('SF', 'Не крита парковка'), ('SM', 'Багатоповерхова парковка')], max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='number',
            field=models.IntegerField(default=0, unique=True, verbose_name='Номер автостояночного місця'),
        ),
    ]