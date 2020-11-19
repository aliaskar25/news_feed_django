from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostModelForm

from django.contrib.sites.shortcuts import get_current_site


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return Post.objects.select_related('blog', 'blog__user').all().order_by('-id')

    
class MyFeedView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        current_user = self.request.user
        qs = Post.objects.select_related('blog', 'blog__user').\
             filter(blog__user__in=current_user.follows.all()).\
             order_by("-id")
        return qs


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostModelForm
    queryset = Post.objects.all()

    def post(self, request):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                blog=request.user.blog
            )
            post.save()
            return redirect('posts_list_url')
        return render(request, self.template_name, {'form': form})


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post_detail.html'


def read(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            if request.user == post.blog.user:
                return redirect('post_detail_url', pk=pk)
            post.user_read.add(request.user)
    return redirect('post_detail_url', pk=pk)
