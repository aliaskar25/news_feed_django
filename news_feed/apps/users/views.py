from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import User


class UserDetail(DetailView):
    model = User
    template_name = 'users/user.html'


def follow(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)

        if request.user.is_authenticated:
            if request.user.pk == user.pk:
                return redirect('user_detail_url', pk=user.pk)

            if request.user in user.followers.all():
                user.followers.remove(request.user)
            else:
                user.followers.add(request.user)
    return redirect('user_detail_url', pk=user.pk)
