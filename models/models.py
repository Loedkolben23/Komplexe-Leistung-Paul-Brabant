from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.core.cache import cache

class shool(models.Model):
    name = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    founded = models.DateField(auto_now_add=True)
    school_type = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super(shool, self).save(*args, **kwargs)
        cache.clear()
