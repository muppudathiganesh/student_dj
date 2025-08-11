# sms_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student, Enrollment, Assignment

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'due_date', 'document']
