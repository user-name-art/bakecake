from django.contrib import admin

from .models import CustomUser, Order, Cake, Composition, CompositionType


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cost',)
    raw_id_fields = ('user', 'cakes', 'compositions',)


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    pass


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    pass


@admin.register(CompositionType)
class CompositionTypeAdmin(admin.ModelAdmin):
    pass
