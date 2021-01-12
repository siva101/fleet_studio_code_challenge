'''
Author:Sivaperumal.M
Date:13.01.2021
Description: Registered the CustomUSerModel in Admin
'''

from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)


# Register your models here.
