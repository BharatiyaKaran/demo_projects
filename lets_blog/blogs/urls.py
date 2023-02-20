from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogs import views

urlpatterns = [
    path('', views.BlogList.as_view(), name="all_blogs" ),
    path('<int:pk>/', views.BlogDetail.as_view(), name="user_blogs"),
]

urlpatterns = format_suffix_patterns(urlpatterns)