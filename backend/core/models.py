from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUserModel(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)