from django.utils import timezone
from django.http import JsonResponse
from .models import RateLimit

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        if self.is_rate_limited(ip_address):
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        self.log_request(ip_address)
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def is_rate_limited(self, ip_address):
        try:
            rate_limit = RateLimit.objects.get(ip_address=ip_address)
            rate_limit.update_request_count()
            return rate_limit.is_rate_limited()
        except RateLimit.DoesNotExist:
            RateLimit.objects.create(ip_address=ip_address, request_count=1, last_request=timezone.now())
            return False

    def log_request(self, ip_address):
        try:
            rate_limit = RateLimit.objects.get(ip_address=ip_address)
            rate_limit.update_request_count()
        except RateLimit.DoesNotExist:
            RateLimit.objects.create(ip_address=ip_address, request_count=1, last_request=timezone.now())
