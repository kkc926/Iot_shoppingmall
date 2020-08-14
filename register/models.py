from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
import datetime


# Custom User model/Manager definition

# class UserManager(BaseUserManager):
#     use_in_migrations = True
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('must have user email')
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username
#         )
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password
#         )
#         user.is_admin = True
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#
# class User(AbstractBaseUser,PermissionsMixin):
#     objects = UserManager()
#
#     email = models.EmailField(
#         max_length=255,
#         unique=True,
#     )
#     username = models.CharField(
#         max_length=20,
#         null=False,
#         unique=True
#     )
#     birthdate = models.DateField(default=datetime.datetime.now().date())
#     addr = models.CharField(max_length=100)
#     phone = models.CharField(max_length=11) #validate at Frontend
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#
#     date_joined = models.DateTimeField(auto_now_add=True)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']