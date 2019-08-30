from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


class PostListView(ListView):
    """class based view for viewing the blog page"""
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 4


class CategoryListView(PostListView):
    """class based view for viewing posts for specific category """

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs['category'])


class PostDetailView(DetailView):
    """class based view for individual blog post"""
    model = Post
    context_object_name = "post"
    template_name = 'blog/view_post.html'


class PostCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """class view for creating new posts.
    It redirects you to the login page if user not logged in"""
    model = Post
    permission_required = 'blog.can_add'
    fields = ['title', 'post_photo', 'content', 'category']
    template_name = 'blog/new_post.html'
    success_message = 'New post created successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """class view for updating posts."""
    model = Post
    permission_required = 'blog.can_add'
    template_name = 'blog/new_post.html'
    fields = ['title', 'post_photo', 'content']
    success_message = 'Post updated successful'


class PostDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """class based view for deleting any individual blog post"""
    model = Post
    permission_required = 'blog.can_delete'
    success_url = '/blog/'
    template_name = 'blog/delete_post.html'
    success_message = 'Post deleted successful'

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author or self.request.user.is_staff:
    #         return True
    #     return False
