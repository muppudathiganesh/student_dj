# sms_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Student, Teacher, Course, Enrollment, Attendance, Grade, Timetable, Assignment, Notification
from .forms import UserRegistrationForm, StudentRegistrationForm, EnrollmentForm, AssignmentUploadForm
from django.db.models import Avg
import csv
from django.template.loader import render_to_string
# sms_app/views.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.http import HttpResponse
from .models import Enrollment

def register_student(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegistrationForm()
        student_form = StudentRegistrationForm()
    return render(request, 'sms_app/register_student.html', {'user_form': user_form, 'student_form': student_form})

@login_required
def dashboard(request):
    user = request.user
    context = {}
    if hasattr(user, 'student'):
        enrollments = user.student.enrollments.all()
        context['enrollments'] = enrollments
    elif hasattr(user, 'teacher'):
        courses = user.teacher.course_set.all()
        context['courses'] = courses
    return render(request, 'sms_app/dashboard.html', context)

@login_required
def enroll_course(request):
    if not hasattr(request.user, 'student'):
        return HttpResponse("Unauthorized", status=401)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user.student
            enrollment.save()
            return redirect('dashboard')
    else:
        form = EnrollmentForm()
    return render(request, 'sms_app/enroll_course.html', {'form': form})

@login_required
def attendance_calendar(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    attendances = enrollment.attendances.all()
    return render(request, 'sms_app/attendance_calendar.html', {'attendances': attendances, 'enrollment': enrollment})

@login_required
def gradebook(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    grades = enrollment.grades.all()
    avg_score = grades.aggregate(Avg('score'))['score__avg']
    return render(request, 'sms_app/gradebook.html', {'grades': grades, 'enrollment': enrollment, 'avg_score': avg_score})

@login_required
def upload_assignment(request):
    if not hasattr(request.user, 'teacher'):
        return HttpResponse("Unauthorized", status=401)
    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AssignmentUploadForm()
    return render(request, 'sms_app/upload_assignment.html', {'form': form})

@login_required
def export_csv(request):
    # Example export students enrolled in a course
    if not hasattr(request.user, 'teacher'):
        return HttpResponse("Unauthorized", status=401)
    course_id = request.GET.get('course_id')
    course = get_object_or_404(Course, id=course_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{course.code}_enrollments.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Student Name', 'Email', 'Enrollment Date'])
    for enrollment in course.enrollments.all():
        writer.writerow([enrollment.student.user.get_full_name(), enrollment.student.user.email, enrollment.enrolled_on])
    return response



@login_required
def export_pdf(request):
    enrollment_id = request.GET.get('enrollment_id')
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    grades = enrollment.grades.all()
    user = request.user
    if not (
        (hasattr(user, 'student') and user.student == enrollment.student)
        or (hasattr(user, 'teacher') and enrollment.course.teacher == user.teacher)
    ):
        return HttpResponse("Unauthorized", status=401)

    # Create the HttpResponse object with PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="gradebook_{enrollment.id}.pdf"'

    # Create the PDF object, using the response as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(1*inch, height - 1*inch, f"Gradebook for {enrollment.student.user.get_full_name()}")
    p.drawString(1*inch, height - 1.3*inch, f"Course: {enrollment.course.name} ({enrollment.course.code})")

    # Table header
    p.setFont("Helvetica-Bold", 12)
    y = height - 1.8*inch
    p.drawString(1*inch, y, "Assignment")
    p.drawString(4*inch, y, "Score")
    p.drawString(5*inch, y, "Max Score")
    p.line(1*inch, y-5, 6*inch, y-5)

    # Table content
    p.setFont("Helvetica", 12)
    y -= 0.3*inch
    for grade in grades:
        p.drawString(1*inch, y, grade.assignment_name)
        p.drawString(4*inch, y, f"{grade.score:.1f}")
        p.drawString(5*inch, y, f"{grade.max_score:.1f}")
        y -= 0.25*inch
        if y < 1*inch:  # start new page if needed
            p.showPage()
            y = height - 1*inch

    # Save the PDF
    p.showPage()
    p.save()

    return response

