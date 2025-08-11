# sms_app/admin.py
from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment, Attendance, Grade, Timetable, Assignment, Notification

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(Timetable)
admin.site.register(Assignment)
admin.site.register(Notification)
