from django.contrib import admin

from .models import CustomUser, Order, Cake, Decor, Berry, Shape, Topping, Level, CustomCake


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'cakes', 'custom_cake')


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    pass


@admin.register(Decor, Berry, Shape, Topping, Level)
class CakePartsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    list_editable = ['price']


@admin.register(CustomCake)
class CustomCakeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'topping', 'berry', 'decor', 'text')
