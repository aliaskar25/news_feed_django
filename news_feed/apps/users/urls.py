from django.urls import path

from .views import UserDetail, follow


urlpatterns = [
    path('<int:pk>/', UserDetail.as_view(), name='user_detail_url'),
    path('<int:pk>/follow/', follow, name='follow-toggle'),
]