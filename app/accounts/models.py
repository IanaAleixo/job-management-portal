from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from app.accounts.managers import UserManager
from app.common import choices

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255,verbose_name="Name")
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False, help_text=("Designates whether the user can log into this admin site."),)
    is_active = models.BooleanField(default=True,help_text=("Designates whether this user should be treated as active. Unselect this instead of deleting accounts."), verbose_name="Ativo?",)
    type = models.PositiveIntegerField(choices=choices.TYPE_USER, blank=True, default=0, verbose_name="User type", editable=False)
    expected_salary = models.CharField(max_length=255, choices=choices.SALARY_RANGE,  default=choices.SALARY_RANGE.up_to_1000, null=True, verbose_name="Expected salary")
    experience = models.CharField(max_length=255, blank=True, null=True, verbose_name="Experience")
    last_education = models.CharField(max_length=255, choices=choices.SCHOOLING, blank=True, null=True, verbose_name="Last Education")
    USERNAME_FIELD = "email"
    
    objects = UserManager()

    def __str__(self) -> str:
        return self.name

class ManagerUser(models.Manager):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop("type", True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(type=self.type)

    def create(self, **kwargs):
        kwargs.update({"type": self.type})
        return super().create(**kwargs)  

class Admin(User):
    objects = ManagerUser(type=choices.TYPE_USER.admin)
    
    class Meta:
        proxy = True
        verbose_name = "Administrador"
        verbose_name_plural = "Administradors"

class Company(User):
    objects = ManagerUser(type=choices.TYPE_USER.company)

    class Meta:
        proxy = True
        verbose_name = "Company manager"
        verbose_name_plural = "Company managers"
    
    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = False
        self.type = 1
        super().save(*args, **kwargs)
        self.groups.add(1)

class Candidate(User):
    objects = ManagerUser(type=choices.TYPE_USER.candidate)

    class Meta:
        proxy = True
        verbose_name = "Candidate"
        verbose_name_plural = "Canditates"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_staff = True
            self.is_superuser = False
            self.type = 2
        super().save(*args, **kwargs)
        self.groups.add(2)
        
