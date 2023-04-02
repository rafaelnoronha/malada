from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

from apps.core.models import Base


USER_TYPE_CHOICES = (
    ('A', 'Admin'),
    ('M', 'Member'),
    ('C', 'Costumer'),
)


class UserManagerCustom(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, Base, PermissionsMixin):
    sr_name = models.CharField(
        verbose_name='Name',
        max_length=150
    )

    sr_email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    sr_observation = models.CharField(
        verbose_name='Observation',
        max_length=4000,
        blank=True
    )

    sr_uuid_password_reset = models.CharField(
        verbose_name='UUID Password Reset',
        max_length=36,
        blank=True
    )

    sr_type = models.CharField(
        verbose_name = 'User type',
        max_length=1,
        choices=USER_TYPE_CHOICES
    )

    username = None
    last_login = None
    is_active = None


    class Meta:
        db_table = 'pj_user'
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    USERNAME_FIELD = 'sr_email'
    EMAIL_FIELD = 'sr_email'
    REQUIRED_FIELDS = ['sr_email',]

    objects = UserManagerCustom()


    class Meta:
        db_table = 'pj_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['sr_type',], name='idx_sr_type')
        ]
