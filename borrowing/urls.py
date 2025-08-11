from django.urls import path
from . import views

app_name = 'borrowing'

urlpatterns = [
    path('', views.borrowing_list, name='borrowing_list'),
]
