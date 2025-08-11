from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'member_id', 'joined_date')
    search_fields = ('full_name', 'email', 'member_id')
