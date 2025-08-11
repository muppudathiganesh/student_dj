from django.db import models

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    member_id = models.CharField(max_length=20, unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
