import string
import random
from urllib.parse import urlparse

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

ALLOWED_SCHEMES = ('http', 'https')
BLOCKED_DOMAINS = ('localhost', '127.0.0.1')  # extend as needed

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class ShortURL(models.Model):
    code = models.CharField(max_length=10, unique=True, db_index=True, blank=True)
    original_url = models.URLField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    visits = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        # Validate scheme
        parsed = urlparse(self.original_url)
        if parsed.scheme not in ALLOWED_SCHEMES:
            raise ValidationError('URL must start with http:// or https://')

        # Block localhost/internal hosts
        hostname = parsed.hostname
        if hostname in BLOCKED_DOMAINS:
            raise ValidationError('This domain is not allowed.')

    def save(self, *args, **kwargs):
        # Run model validation
        self.full_clean()

        # Génération du code si vide
        if not self.code:
            code = generate_code()
            while ShortURL.objects.filter(code=code).exists():
                code = generate_code()
            self.code = code  # ✅ correctement en dehors du while

        super().save(*args, **kwargs)

    def short_link(self, request=None):
        if request:
            base = request.build_absolute_uri('/')[:-1]
            return f"{base}/{self.code}/"
        return self.code

    def __str__(self):
        return f"{self.code} -> {self.original_url}"
