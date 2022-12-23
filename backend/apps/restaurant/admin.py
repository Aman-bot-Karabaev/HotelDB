from django.contrib import admin

from backend.apps.restaurant.models import *

admin.site.register(RestaurantBook)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

