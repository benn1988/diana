# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# def blog(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    """class based view for viewing the blog page"""
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 4

class PostDetailView(DetailView):
    """class based view for individual blog post"""
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    """class view for creating new posts.
    It redirects you to the login page if user not logged in"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """class view for updating posts.
    It does not allow you to edit other user`s posts"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """class based view for deleting any individual blog post.
    Does not allow different user to delete the post, except the author"""
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
