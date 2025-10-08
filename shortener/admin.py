from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('code', 'original_url', 'owner', 'visits', 'is_active', 'created_at')
    search_fields = ('code', 'original_url', 'owner__username')
    list_filter = ('is_active',)