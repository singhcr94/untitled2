from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.signals import post_save

class usermanager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError('User is not active')
        user_obj=self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.active=is_active
        user_obj.admin=is_admin
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self,email,password=None):
        user=self.create_user(email,password=password,is_staff=True)
        return user
    def create_superuser(self,email,password=None):
        user=self.create_user(email,password=password,is_staff=True,is_admin=True)
        return user

class customuser(AbstractBaseUser):
    email=models.EmailField(max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects=usermanager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=15)
    dob=models.DateField(max_length=8)
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    def __str__(self):
        return  self.firstname
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=person.objects.create(firstname=kwargs['instance'])
post_save.connect(create_profile,sender=User)