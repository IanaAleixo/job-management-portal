from django.contrib import admin
from app.jobs.models import Job


@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    """Job"""
    
    list_display  = ("name", "salary_range", "requirements", "schooling")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)

