from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'news', viewsets.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', viewsets.CustomAuthTokenView.as_view(), name='api_token'),
]