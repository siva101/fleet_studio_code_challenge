
'''
Author:Sivaperumal.M
Date:13.01.2021
Description: Helper functions for User Autentication and Creation
'''

from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model


def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user



def create_user_account(username, password,  **extra_fields):
    user = get_user_model().objects.create_user(username=username, password=password, **extra_fields)
    return user