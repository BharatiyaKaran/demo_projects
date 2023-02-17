from django.db import models
from .base import TimeStamp
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Publised')
)

class Blog(TimeStamp):
    title = models.CharField(max_length=255, blank=False, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def slug(self):
        return slugify(self.title)
