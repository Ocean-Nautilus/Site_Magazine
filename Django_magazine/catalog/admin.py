from django.contrib import admin
from .models import Category, Poster

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Автоматически заполняет slug из имени категории (например, "Ретро плакаты" -> "retro-plakaty")
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'category')
    search_fields = ('title', 'description')