from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
import oauth2_provider.models

from .views import ProductViewSet, UserCreate, UserViewSet, activate

try:
    oauth2_app = oauth2_provider.models.Application()
    oauth2_app.client_id = "id"
    oauth2_app.client_secret = "secret"
    oauth2_app.name = "name"
    oauth2_app.client_type = "confidential"
    oauth2_app.authorization_grant_type = "password"
    oauth2_app.save()
except Exception as e:
    print(e)

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('createUser/', UserCreate.as_view()),
    path('oauth/', include('oauth2_provider.urls')),
    path('activate/<int:pk>/<str:token>/', activate)
]
