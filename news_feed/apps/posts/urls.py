from django.urls import path

from .views import PostList


urlpatterns = [
    path('', PostList.as_view(), name='posts_list_url'), 
]