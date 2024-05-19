from django.contrib import admin
from .models import RateLimit

@admin.register(RateLimit)
class RateLimitAdmin(admin.ModelAdmin):
    list_display = ('masked_ip_address', 'request_count', 'last_request')
    list_filter = ('ip_address', 'last_request')
    search_fields = ('ip_address',)
    ordering = ('-last_request',)

    def masked_ip_address(self, obj):
        # Dividimos o endereço IP em partes e mascaramos os últimos números
        parts = obj.ip_address.split('.')
        if len(parts) == 4:
            return f"{parts[0]}.***.***.***"
        else:
            # Caso o endereço IP não esteja no formato IPv4
            return "Invalid IP"

    masked_ip_address.short_description = 'IP Address'
