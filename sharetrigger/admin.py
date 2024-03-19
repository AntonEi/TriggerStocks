from django.contrib import admin
from .models import sharetrigger

class ShareTriggerAdmin(admin.ModelAdmin):
    list_display = ('suggest_stock', 'author', 'suggest_date', 'created_on')
    list_filter = ('suggest_date',)
    search_fields = ('suggest_stock', 'author__username')

admin.site.register(sharetrigger, ShareTriggerAdmin)
