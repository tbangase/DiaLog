from django.db import models

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class CustomUserManager(UserManager):
  user_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('Sorry, We need Email.')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self._create_user(email,password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  email       = models.EmailField('email address', unique=True)
  name        = models.CharField(max_length=100)

  created_at  = models.DateTimeField('user created')
  updated_at  = models.DateTimeField('user updated')
  level       = models.IntegerField(default=0)
  exp         = models.IntegerField(default=0)

  is_staff = models.BooleanField(
    'staff status',
    default=False,
    help_text='Designates whether the user can log into this admin site',
  )

  is_active = models.BooleanField(
    'active',
    default=False,
    help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
  )

  objects = CustomUserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELD = []
  
  def email_user(self, subject, message, from_email=None, **kwargs):
    """Send email to this user"""
    send_mail(subject, message, from_email, [self.email], **kwargs)

  def __str__(self):
    return self.name


class Diary(models.Model):
  user        = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at  = models.DateTimeField('diary created')
  title       = models.CharField(max_length= 200, default="")
  content     = models.CharField(max_length= 2000)

  def __str__(self):
    return self.title

