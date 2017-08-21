from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'real_name', 'email', 'moderator')
    search_fields = ('username', 'email')
    ordering = ('id',)
    list_filter = ('moderator',)
    fields = ('username', 'moderator')

admin.site.register(User, UserAdmin)