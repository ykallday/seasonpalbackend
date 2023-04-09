from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithLocView, CustomUserCreate, RestrictedView

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('restricted/', RestrictedView.as_view(), name = 'restricted'),
    path('token/obtain/', ObtainTokenPairWithLocView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk/', views.UserDetail.as_view(), name='user_detail'),
    path('produce/', views.ProduceList.as_view(), name='produce_list'),
    path('produce/<int:pk/', views.ProduceDetail.as_view(), name='produce_detail')
]