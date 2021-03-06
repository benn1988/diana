"""diana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('category/<category>/', CategoryListView.as_view(), name='category'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/update/<str:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<str:slug>/', PostDeleteView.as_view(), name='post-delete'),
]
