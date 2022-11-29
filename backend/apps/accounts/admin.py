from django.contrib import admin
from backend.apps.accounts.models import User, Comment

@admin.register(User)
class RoomsAdmin(admin.ModelAdmin):
    context = User.objects.all()
                                

admin.site.register(Comment)