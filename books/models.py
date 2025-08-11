from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    barcode = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_available(self):
        return self.available_copies > 0
