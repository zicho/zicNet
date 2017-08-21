from django.contrib import admin
from .models import Feed_entry

# Register your models here.

class Feed_entryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'publish_date')
    search_fields = ('author', 'body')
    ordering = ('-id',)

admin.site.register(Feed_entry, Feed_entryAdmin)
