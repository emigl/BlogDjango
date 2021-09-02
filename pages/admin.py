from django.contrib import admin
from .models import Page

# extra conf

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    # Search bar
    search_fields = ('title', 'content')
    # Filter by Visible (Yes, No)
    list_filter = ('visible',)
    list_display = ('title', 'created_at', 'visible')
    ordering = ('-created_at',)

# Register your models here.

admin.site.register(Page, PageAdmin)

# Name config panel
title = "Django Blog Proyect"
subtitle = "Admin Panel"

admin.site.site_header = title

admin.site.site_title = title

admin.site.index_title = subtitle