from django.contrib import admin

# Register your models here.

from backend.apps.rooms.models import *


admin.site.register(Booking)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]



admin.site.register(Contact)
class RoomsAdmin(admin.ModelAdmin):
    context = User.objects.all()

    

admin.site.register(Rooms)

admin.site.register(RoomImage)
