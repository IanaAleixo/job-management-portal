from django.db import models
from app.common import choices

class Job(models.Model):
    name = models.CharField(max_length=255,verbose_name="Name")
    salary_range = models.CharField(max_length=255 ,choices=choices.SALARY_RANGE, blank=True, default=choices.SALARY_RANGE.up_to_1000, verbose_name="Salary range", editable=True)
    requirements = models.TextField(max_length=255, verbose_name="Requirements")
    schooling = models.CharField(max_length=250, choices=choices.SCHOOLING, blank=True, default=choices.SCHOOLING.Elementary_School, verbose_name="Schooling", editable=True)
    is_active = models.BooleanField(default=True,help_text=("Designates whether this job should be treated as active. Unselect this instead of deleting accounts."), verbose_name="Active?")

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs" 

    def __str__(self) -> str:
        return self.name
    
    @property
    def candidates(self):
        return Application.objects.filter(job=self)
    
    @property
    def count_candidates(self):
        return Application.objects.filter(job=self).count()
    

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    expected_salary = models.CharField(choices=choices.SALARY_RANGE, max_length=255, blank=True, null=True, verbose_name="Expected salary")
    experience = models.CharField(max_length=255, blank=True, null=True, verbose_name="Experience")
    last_education = models.CharField(choices=choices.SCHOOLING, max_length=255, blank=True, null=True, verbose_name="Last Education")

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applicantions"
        unique_together = ["job", "user"]
    
    def save(self, *args, **kwargs):
        self.expected_salary = self.user.expected_salary
        self.experience = self.user.experience
        self.last_education = self.user.last_education
        super().save(*args, **kwargs)

    def calculate_job_compatibility(self):
        points = 0
        
        if choices.SALARY_RANGE_DICT.get(self.expected_salary) <= choices.SALARY_RANGE_DICT.get(self.job.salary_range):
            points+=1
        if choices.SCHOOLING_DICT.get(self.last_education) >= choices.SCHOOLING_DICT.get(self.job.schooling):
            points+=1
        return points

    @property
    def job_compatibility(self):
        return self.calculate_job_compatibility()
    