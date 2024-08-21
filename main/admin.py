
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Parking, Parking_Place, Account


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Account'

class ParkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'type')


class ParkingPlaceAdmin(admin.ModelAdmin):
    list_display = ('parking', 'number', 'parking_cost', 'is_place_for_disable', 'is_place_for_electric', 'status', 'reserved_by')


class CustomizeUserAdmin(UserAdmin):
    inlines = (AccountInline, )
    list_display = ('username', 'email', 'phone_number', 'is_staff',)

    def phone_number(self,obj):
        return str(obj.account.phone_number)


admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)

admin.site.register(Parking, ParkingAdmin)
admin.site.register(Parking_Place, ParkingPlaceAdmin)
