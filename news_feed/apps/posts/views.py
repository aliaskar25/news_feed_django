from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostModelForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        print(self.request.user)
        if not self.request.user.is_anonymous:
            current_user = self.request.user
            qs = Post.objects.select_related('blog', 'blog__user').filter(blog__user__in=current_user.follows.all())
            qs = qs.order_by("-id")
            return qs
        return Post.objects.select_related('blog', 'blog__user').all().order_by('-id')


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostModelForm
    queryset = Post.objects.all()

    def post(self, request):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            post = form.save()
            post.blog = request.user.blog
            post.save()
            return redirect('posts_list_url')
        return render(request, self.template_name, {'form': form})


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post_detail.html'
