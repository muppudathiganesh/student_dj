from datetime import date
from library_app.models import Book, Member, BorrowRecord, Reservation  # replace library_app with your app name

# Create sample books
books = [
    Book.objects.create(isbn='9780140449136', title='The Odyssey', author='Homer', published_year=-800, copies_available=5),
    Book.objects.create(isbn='9780439136365', title='Harry Potter and the Prisoner of Azkaban', author='J.K. Rowling', published_year=1999, copies_available=3),
    Book.objects.create(isbn='9780553293357', title='Dune', author='Frank Herbert', published_year=1965, copies_available=4),
    Book.objects.create(isbn='9780316769488', title='The Catcher in the Rye', author='J.D. Salinger', published_year=1951, copies_available=2),
    Book.objects.create(isbn='9780061120084', title='To Kill a Mockingbird', author='Harper Lee', published_year=1960, copies_available=6),
]

# Create sample members
members = [
    Member.objects.create(member_id='M001', name='Alice Johnson', email='alice@example.com', phone='555-1234', registration_date=date(2024, 1, 15)),
    Member.objects.create(member_id='M002', name='Bob Smith', email='bob@example.com', phone='555-5678', registration_date=date(2024, 2, 10)),
    Member.objects.create(member_id='M003', name='Carol Lee', email='carol@example.com', phone='555-8765', registration_date=date(2024, 3, 22)),
]

# Create sample borrowing records
borrow_records = [
    BorrowRecord.objects.create(borrow_id='B001', member=members[0], book=books[0], borrow_date=date(2024, 7, 1), due_date=date(2024, 7, 15), return_date=date(2024, 7, 14), fine_amount=0),
    BorrowRecord.objects.create(borrow_id='B002', member=members[1], book=books[1], borrow_date=date(2024, 7, 3), due_date=date(2024, 7, 17), return_date=date(2024, 7, 20), fine_amount=3),
    BorrowRecord.objects.create(borrow_id='B003', member=members[2], book=books[3], borrow_date=date(2024, 7, 5), due_date=date(2024, 7, 19), return_date=None, fine_amount=0),
]

# Create sample reservations
reservations = [
    Reservation.objects.create(reservation_id='R001', member=members[1], book=books[2], reservation_date=date(2024, 7, 10), status='Pending'),
    Reservation.objects.create(reservation_id='R002', member=members[0], book=books[4], reservation_date=date(2024, 7, 12), status='Completed'),
]

print("Sample data created successfully.")
