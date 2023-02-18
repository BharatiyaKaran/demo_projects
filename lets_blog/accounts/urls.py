from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views
from rest_framework_simplejwt.views import(
    TokenRefreshView, 
    TokenVerifyView, 
    TokenObtainPairView )

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('user_profiles/', views.UserProfileList.as_view(), name="get_user_profile_list"),
    path('user_profiles/<int:pk>/', views.UserProfileDetail.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
]

urlpatterns = format_suffix_patterns(urlpatterns)