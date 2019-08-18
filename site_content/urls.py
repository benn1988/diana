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
from .views import (
    ServicesView,
    GalleryView,
    ContactView,
    IndexView,
    PhotoUploadView,
    PhotoDeleteView,
    PhotoEditView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('gallery/upload/', PhotoUploadView.as_view(), name='photo-upload'),
    path('gallery/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('gallery/<int:pk>/edit/', PhotoEditView.as_view(), name='photo-edit'),
]
