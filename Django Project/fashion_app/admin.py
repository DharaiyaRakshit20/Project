from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Register)
admin.site.register(Cart)
admin.site.register(Details)
# class CartAdmin(admin.ModelAdmin):
#     list_display =[__all__] 