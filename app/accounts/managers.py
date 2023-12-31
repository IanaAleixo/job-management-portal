from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create(self, **kwargs):
        if self.type:
            kwargs.update({"type": self.type})
        user = super().create(**kwargs)
        user.set_password(kwargs.get("password"))
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **kwargs):
        request = None
        if "request" in kwargs:
            request = kwargs.pop("request")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.kind = 0
        user.save(using=self._db)
        return user