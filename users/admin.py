from django.contrib import admin
from .models import User_profile, private_message

# Register your models here.

class User_profileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')
    search_fields = ('owner',)
    ordering = ('owner',)

class private_messageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient')
    search_fields = ('owner', 'recipient')
    ordering = ('sender',)	
	
admin.site.register(User_profile, User_profileAdmin)
admin.site.register(private_message, private_messageAdmin)