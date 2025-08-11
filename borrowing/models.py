from django.db import models
from django.utils import timezone
from books.models import Book
from members.models import Member
from datetime import timedelta

class BorrowingRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    returned_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.borrowed_at + timedelta(days=14)  # 2 weeks default
        super().save(*args, **kwargs)

    def is_overdue(self):
        if self.returned_at:
            return self.returned_at > self.due_date
        return timezone.now().date() > self.due_date

    def fine_amount(self):
        if self.returned_at and self.returned_at > self.due_date:
            days_late = (self.returned_at - self.due_date).days
            return days_late * 5
        elif not self.returned_at and timezone.now().date() > self.due_date:
            days_late = (timezone.now().date() - self.due_date).days
            return days_late * 5
        return 0

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.full_name}"
