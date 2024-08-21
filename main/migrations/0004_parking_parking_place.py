# Generated by Django 3.2.7 on 2024-04-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20240417_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('street', models.CharField(max_length=100, verbose_name='Вулиця')),
                ('count', models.IntegerField(verbose_name='Кількість паркомісць')),
                ('type', models.CharField(choices=[('SF', 'Surface parking'), ('SM', 'Surface multi-storey parking'), ('UG', 'underground parking')], max_length=2, verbose_name='Тип')),
                ('lat', models.FloatField(max_length=35, verbose_name='Широта')),
                ('lng', models.FloatField(max_length=35, verbose_name='Довгота')),
                ('img', models.ImageField(upload_to='main/parking/images')),
                ('info', models.TextField(default='', max_length=500, verbose_name='Інформація')),
            ],
        ),
        migrations.CreateModel(
            name='Parking_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_place_for_disable', models.BooleanField(default=False, verbose_name='Місце для інвалідів')),
                ('is_place_for_electric', models.BooleanField(default=False, verbose_name='Місце з підзарядкою')),
                ('distance_to_exit', models.IntegerField(verbose_name='Відстань до виїзду')),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.parking')),
            ],
        ),
    ]
