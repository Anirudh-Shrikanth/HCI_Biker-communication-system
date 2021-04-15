from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django_bleach.models import BleachField

# Create your models here.

class Messages(models.Model):
    chat_room = BleachField(
        max_length=50,
    )
    user =  BleachField(
        max_length=50,
    )
    data = BleachField(
        max_length=1000,
    )