from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    biography = models.TextField()
    linkedin = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
