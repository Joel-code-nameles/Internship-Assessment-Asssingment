from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=255, null=True, blank=False)
    password = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return self.username