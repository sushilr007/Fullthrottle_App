from django.conf.urls import url
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('activity_period', ActivityPeriodViewSet)

urlpatterns = router.urls