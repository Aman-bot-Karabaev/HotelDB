from django.contrib import admin

from backend.apps.restaurant.models import *
admin.site.register(RestaurantBook)
admin.site.register(RestaurantMenu)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

