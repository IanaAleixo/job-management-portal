from django.contrib import admin
from app.jobs.models import Job, Application


@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    """Job"""
    
    list_display  = ("name", "salary_range", "requirements", "schooling")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("name", "salary_range", "requirements", "schooling")}),)


@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    """Application"""
    
    list_display  = ("job", "user", "expected_salary", "experience", "last_education")
    search_fields = ("job__name",)
    ordering = ("job__name",)
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("job", "user", "expected_salary", "experience", "last_education")}),)


