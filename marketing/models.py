from django.db import models

class WaitlistSignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

