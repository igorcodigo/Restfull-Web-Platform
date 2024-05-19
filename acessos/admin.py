from django.contrib import admin
from .models import RateLimit

@admin.register(RateLimit)
class RateLimitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'request_count', 'last_request')
    list_filter = ('ip_address', 'last_request')
    search_fields = ('ip_address',)
    ordering = ('-last_request',)
