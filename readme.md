from django.contrib.auth.models import User
from sms_app.models import Student, Teacher, Course, Enrollment, Grade

# Create a teacher user and teacher profile
teacher_user = User.objects.create_user(username='teacher1', email='teacher1@example.com', password='testpass123')
teacher = Teacher.objects.create(user=teacher_user, department='Mathematics')

# Create a few courses
course_math = Course.objects.create(name='Algebra I', code='MATH101', teacher=teacher)
course_physics = Course.objects.create(name='Physics I', code='PHYS101', teacher=teacher)

# Create student users and profiles
student_user1 = User.objects.create_user(username='student1', email='student1@example.com', password='testpass123')
student1 = Student.objects.create(user=student_user1, roll_number='S1001', department='Mathematics')

student_user2 = User.objects.create_user(username='student2', email='student2@example.com', password='testpass123')
student2 = Student.objects.create(user=student_user2, roll_number='S1002', department='Physics')

# Enroll students in courses
enrollment1 = Enrollment.objects.create(student=student1, course=course_math)
enrollment2 = Enrollment.objects.create(student=student2, course=course_physics)

# Add grades for enrollments
Grade.objects.create(enrollment=enrollment1, assignment_name='Homework 1', score=85, max_score=100)
Grade.objects.create(enrollment=enrollment1, assignment_name='Quiz 1', score=90, max_score=100)
Grade.objects.create(enrollment=enrollment2, assignment_name='Homework 1', score=88, max_score=100)
Grade.objects.create(enrollment=enrollment2, assignment_name='Quiz 1', score=92, max_score=100)

print("Sample data created successfully!")
