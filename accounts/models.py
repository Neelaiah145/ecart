from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    
    