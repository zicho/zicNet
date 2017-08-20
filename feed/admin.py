from django.contrib import admin
from .models import Feed_entry

# Register your models here.

<<<<<<< HEAD
class Feed_entryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'publish_date')
    search_fields = ('author', 'body')
    ordering = ('-id',)

admin.site.register(Feed_entry, Feed_entryAdmin)
=======
admin.site.register(Feed_entry)
>>>>>>> 076d7e50dd2c996a3e670abd34afa6fc54aaf74f
