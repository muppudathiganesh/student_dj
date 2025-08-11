# sms_app/urls.py
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enroll/', views.enroll_course, name='enroll_course'),
    path('attendance/<int:enrollment_id>/', views.attendance_calendar, name='attendance_calendar'),
    path('gradebook/<int:enrollment_id>/', views.gradebook, name='gradebook'),
    path('upload-assignment/', views.upload_assignment, name='upload_assignment'),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
]
