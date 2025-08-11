from django.contrib import admin
from .models import BorrowingRecord

@admin.register(BorrowingRecord)
class BorrowingRecordAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'borrowed_at', 'due_date', 'returned_at')
    search_fields = ('member__full_name', 'book__title')
