from django.urls import path

from .views import (
    PostListView, PostCreateView,
    PostDetailView, 
)

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_url'), 
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail_url'), 
]