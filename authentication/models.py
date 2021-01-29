# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(blank=True, null=True)


# Create your models here.
