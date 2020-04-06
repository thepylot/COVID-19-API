from django.urls import path, include
from rest_framework.routers import DefaultRouter

from covid19 import views

router = DefaultRouter()
router.register('countries', views.CovidViewSet)

app_name = 'covid19'

urlpatterns = [
    path('', include(router.urls))
]
