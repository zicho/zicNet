from django.contrib import admin
from .models import User_profile

# Register your models here.

class User_profileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')
    search_fields = ('owner',)
    ordering = ('owner',)

admin.site.register(User_profile, User_profileAdmin)