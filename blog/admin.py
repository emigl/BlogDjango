from django.contrib import admin
from .models import Category, Article


# Extra conf




class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'content')
    # Filter by Visible (Yes, No)
    
    list_display = ('name', 'created_at')
    ordering = ('-created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ( 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')
    # Filter by Visible (Yes, No)
    list_filter = ( 'categories__name','user__username','public')
    list_display = ('title', 'created_at', 'user', 'public')
    ordering = ('-created_at',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)