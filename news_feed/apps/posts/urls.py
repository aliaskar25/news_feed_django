from django.urls import path

from .views import (
    PostListView, PostCreateView,
    PostDetailView, read, MyFeedView
)

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_url'), 
    path('me_feed/', MyFeedView.as_view(), name='my_feed_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail_url'), 
    path('<int:pk>/read/', read, name='read-post-url'),
]