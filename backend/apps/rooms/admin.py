from django.contrib import admin

# Register your models here.

from backend.apps.rooms.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ImageAdmin(admin.ModelAdmin):
        pass


class RoomImageInline(admin.StackedInline):
    model = RoomImage
    max_num = 10
    extra = 0


class RoomAdmin(admin.ModelAdmin):
  inlines = [RoomImageInline]

admin.site.register(RoomImage, ImageAdmin)
admin.site.register(Rooms, RoomAdmin)