from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class UserManager(BaseUserManager):
    """Manager for user."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a ne user."""
        if not email:
            raise ValueError('Users must have email address.')
        # self.model refers to a User
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # using=self._db - just in case of adding multiple databases
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Dot(models.Model):
    """DotPrivate object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='dots_private',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    description = models.TextField(max_length=350, blank=True)
    lon = models.IntegerField()
    lat = models.IntegerField()
    rating = models.FloatField(
                    validators=[MinValueValidator(0.0),
                                MaxValueValidator(5.0)])
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
