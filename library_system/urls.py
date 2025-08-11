from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('members/', include('members.urls')),
    path('borrowing/', include('borrowing.urls')),
]
