'''
Author:Sivaperumal.M
Date:13.01.2021
Description: Add the Router Config for URL mappings
'''


from rest_framework import routers

from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = router.urls