from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.posts.urls')),
    path('users/', include('apps.users.urls')), 
]
