from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'posts/posts.html'

    def get_queryset(self):
        print(self.request.user)
        if not self.request.user.is_anonymous:
            current_user = self.request.user
            qs = Post.objects.select_related('blog', 'blog__user').filter(blog__user__in=current_user.follows.all())
            qs = qs.order_by("-id")
            return qs
        return Post.objects.select_related('blog', 'blog__user').all().order_by('-id')
