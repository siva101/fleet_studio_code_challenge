'''
Author:Sivaperumal.M
Date:13.01.2021
Description: Created the CustomUSer Model by inheriting the AsbstarcUser in built from Django
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField('username', max_length=8, null=False,unique=True)
    password=models.CharField('Password', max_length=6, null=False)
    email = models.EmailField('Email address', unique=True)
    full_name = models.CharField('Full Name', max_length=255, null=False)
    mobileno=models.IntegerField('Mobile No', null=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username}"