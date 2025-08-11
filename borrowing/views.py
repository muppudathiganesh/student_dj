from django.shortcuts import render
from .models import BorrowingRecord

def borrowing_list(request):
    records = BorrowingRecord.objects.select_related('member', 'book').all()
    return render(request, 'borrowing/borrowing_list.html', {'records': records})
