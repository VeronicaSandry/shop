from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from detetime import timedelta
def get_future():
    return timezone.now() + timedelta(hours=72)
 
class User(AbstractUser):
    phone = models.CharField(
        max_length=12,
        verbose_name='phone',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=False
    )

    activation_code = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='code for activation'
    )
    activation_code_expires = models.DateTimeField(
        default=get_future
    )
    email = models.EmailField('email address', blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.email

    @property 
    def is_activation_code_expired(self):
        return timezone.now() > self.activation_code_expires

