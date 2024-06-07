from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'author')

# Alternativamente, você pode registrar diretamente sem o decorador
# admin.site.register(Book, BookAdmin)
