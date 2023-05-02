from django.contrib import admin
from .models import Category, Advert

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['created', 'name']
    search_fields = []
    # list_filter = ['status']
    # list_display_links = ['email']
    list_per_page = 100

admin.site.register(Category, CategoryAdmin)

class AdvertAdmin(admin.ModelAdmin):
    list_display = ['created', 'poster', 'title', 'status']
    search_fields = ['title', 'abstract']
    # list_filter = ['status']
    # list_display_links = ['email']
    list_per_page = 100

admin.site.register(Advert, AdvertAdmin)
