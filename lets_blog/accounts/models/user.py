from django.db import models
from django.contrib.auth.models import User
from .base import TimeStamp


class UserProfile(TimeStamp):
    
    DEFAULT_PROFILE_PIC_URL = ""
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    about = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
