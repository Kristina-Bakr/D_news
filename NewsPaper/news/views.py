from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    sort = '-post_creation'
    context_object_name = 'posts'
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'