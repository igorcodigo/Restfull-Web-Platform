from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title