from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    short = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'code', 'short', 'visits', 'is_active', 'created_at']

    def get_short(self, obj):
        request = self.context.get('request')
        return obj.short_link(request)
