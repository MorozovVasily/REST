from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, UserCreate, UserViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('createUser/', UserCreate.as_view()),
    path('oauth/', include('oauth2_provider.urls')),
]