from django.contrib import admin
from .models import Brand, Smartphone


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['model', 'price']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Smartphone,PhoneAdmin)