from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from simple_history.models import HistoricalRecords


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.user.username


class Parking(models.Model):
    name = models.CharField("Назва", max_length=100)
    street = models.CharField("Вулиця", max_length=100)
    urls = models.CharField("Посилання на карту", max_length=100, default='')
    count = models.PositiveIntegerField("Кількість паркомісць", default=0)

    PARKING_TYPE = {
        ("SF", "Не крита парковка"),
        ("SM", "Багатоповерхова парковка"),
        ("UG", "Підземна парковка"),
    }
    type = models.CharField("Тип", max_length=2, choices=PARKING_TYPE)

    lat = models.FloatField("Широта", max_length=35)
    lng = models.FloatField("Довгота", max_length=35)

    img = models.ImageField(upload_to="main/parking/images")
    info = models.TextField("Інформація", max_length=500, default="")

    def __str__(self):
        return self.name


class Parking_Place(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    number = models.IntegerField("Номер автостояночного місця", default=0,
                                 validators=[MinValueValidator(0)])

    parking_cost = models.IntegerField("Вартість бронювання за годину", default=30)


    start_time_reserved = models.DateTimeField(blank=True, null=True)
    end_time_reserved = models.DateTimeField(blank=True, null=True)


    is_place_for_disable = models.BooleanField("Місце для інвалідів", default=False)
    is_place_for_electric = models.BooleanField("Місце з підзарядкою", default=False)
    distance_to_exit = models.PositiveIntegerField("Відстань до виїзду")

    PLACE_STATUS = {
        ("PF", "Місце вільне"),
        ("PT", "Місце зайняте"),
        ("PR", "Місце заброньоване"),
    }

    status = models.CharField("Статус", max_length=2, choices=PLACE_STATUS, default="PF")
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name="Зарезервований")
    reserved_qr = models.ImageField(upload_to="main/parking/qr", null=True, blank=True)

    history = HistoricalRecords()  # new line

    def save(self, *args, **kwargs):
        if not self.reserved_qr.name:
            data = f'{self.parking}___{self.number}'
            qr = qrcode.make(data)
            canvas = Image.new('RGB', (450, 450), 'white')
            ImageDraw.Draw(canvas)
            canvas.paste(qr,(int(canvas.size[0]/2 - qr.size[0]/2), int(canvas.size[1]/2 - qr.size[1] / 2)) )
            fname = data + '.png'

            buf = BytesIO()
            canvas.save(buf, 'PNG')
            self.reserved_qr.save(fname, File(buf), save=False)

            canvas.close()
        super(Parking_Place, self).save(*args, **kwargs)
