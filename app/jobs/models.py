from django.db import models
from app.common import choices

class Job(models.Model):
    name = models.CharField(max_length=255,verbose_name="Name")
    salary_range = models.PositiveIntegerField(choices=choices.SALARY_RANGE, blank=True, default=0, verbose_name="Salary range", editable=True)
    requirements = models.CharField(max_length=255, verbose_name="Requirements")
    schooling = models.PositiveIntegerField(choices=choices.SCHOOLING, blank=True, default=0, verbose_name="Schooling", editable=True)
    is_active = models.BooleanField(default=True,help_text=("Designates whether this job should be treated as active. Unselect this instead of deleting accounts."), verbose_name="Active?")


    def __str__(self) -> str:
        return self.name

