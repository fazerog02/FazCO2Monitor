from rest_framework import routers
from .views import PPMDataViewSet, NowPPMViewSet

router = routers.DefaultRouter()
router.register('ppmdata', PPMDataViewSet)
router.register('nowppm', NowPPMViewSet)
