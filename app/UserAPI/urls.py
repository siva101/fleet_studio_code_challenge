'''
Author:Sivaperumal.M
Date:13.01.2021
Description: Added URL paths for users app
'''
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls'))
]
