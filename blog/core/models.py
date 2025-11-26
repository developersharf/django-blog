from django.db import models    
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def publish(self):
        self.published_at = timezone.now()
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
        