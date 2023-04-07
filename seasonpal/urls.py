from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, RestrictedView

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('restricted/', RestrictedView.as_view(), name = 'restricted'),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]