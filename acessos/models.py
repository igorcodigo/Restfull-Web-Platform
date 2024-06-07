from django.db import models
from django.utils import timezone
from datetime import timedelta

class RateLimit(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    request_count = models.IntegerField(default=0)
    last_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.request_count} requests"

    def reset_request_count(self):
        self.request_count = 0
        self.last_request = timezone.now()
        self.save()

    def increment_request_count(self):
        self.request_count += 1
        self.last_request = timezone.now()
        self.save()

    def is_rate_limited(self):
        return self.request_count > 1200  # Limite de requisições: 100 por 15 minutos

    def update_request_count(self):
        now = timezone.now()
        if now - self.last_request > timedelta(minutes=15):
            self.reset_request_count()
        self.increment_request_count()
