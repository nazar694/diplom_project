# Generated by Django 4.2.11 on 2024-04-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_historicalparking_place_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalparking_place',
            name='parking_time',
        ),
        migrations.RemoveField(
            model_name='parking_place',
            name='parking_time',
        ),
        migrations.AlterField(
            model_name='historicalparking_place',
            name='status',
            field=models.CharField(choices=[('PR', 'Місце заброньоване'), ('PT', 'Місце зайняте'), ('PF', 'Місце вільне')], default='PF', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('UG', 'Підземна парковка'), ('SM', 'Багатоповерхова парковка'), ('SF', 'Не крита парковка')], max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='status',
            field=models.CharField(choices=[('PR', 'Місце заброньоване'), ('PT', 'Місце зайняте'), ('PF', 'Місце вільне')], default='PF', max_length=2, verbose_name='Статус'),
        ),
    ]
