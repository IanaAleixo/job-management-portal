from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.accounts.models import Admin, Company, Candidate

@admin.register(Admin)
class AdminAdmin(UserAdmin):
    """Admin"""

    list_display = ("id", "email", "name")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)

@admin.register(Company)
class AdminCompany(UserAdmin):
    """Company"""

    list_display = ("id", "email", "name")
    list_filter = ("is_active",)
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    
                )
            },
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("name", "email", "password1", "password2")}),)

@admin.register(Candidate)
class AdminCandidate(UserAdmin):
    """Candidate"""

    list_display = ("id", "email", "name")
    list_filter = ("is_active",)
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    
                )
            },
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("name", "email", "password1", "password2", "expected_salary", "experience", "last_education")}),)
