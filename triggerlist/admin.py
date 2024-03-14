from django.contrib import admin
from .models import Trigger, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Trigger)
class TriggerAdmin(SummernoteModelAdmin):

    list_display = ('stock_name', 'slug', 'trigger_date', 'created_on')
    search_fields = ['stock_name']
    list_filter = ('trigger_date',)
    prepopulated_fields = {'slug': ('stock_name',)}
    summernote_fields = ('summary',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('trigger', 'created_on')


