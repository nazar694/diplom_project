# Generated by Django 4.2.11 on 2024-04-29 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0029_alter_parking_type_alter_parking_place_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalparking_place',
            name='status',
            field=models.CharField(choices=[('PF', 'Місце вільне'), ('PT', 'Місце зайняте'), ('PR', 'Місце заброньоване')], default='PF', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='status',
            field=models.CharField(choices=[('PF', 'Місце вільне'), ('PT', 'Місце зайняте'), ('PR', 'Місце заброньоване')], default='PF', max_length=2, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
