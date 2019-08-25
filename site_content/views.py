from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Photo, Photocateg

class IndexView(TemplateView):
    template_name = 'site_content/index.html'

class ServicesView(TemplateView):
    template_name = 'site_content/services.html'

class ContactView(TemplateView):
    template_name = 'site_content/contact.html'

class GalleryView(ListView):
    model = Photo
    template_name = 'site_content/gallery.html'
    paginate_by = 9
    ordering = ['-date_uploaded']

class PhotoUploadView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """class view for uploading new photos.
    It redirects to the login page if user does not have add permission"""
    model = Photo
    permission_required = 'site_content.add_photo'
    fields = ['title', 'photo_full', 'photo_thumbnail', 'categories']
    template_name = 'site_content/photo_upload.html'
    success_message = 'New photo uploaded successfully'
    success_url = '/gallery/'

class PhotoDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """class based view for deleting gallery photo. User needs delete perm"""
    model = Photo
    permission_required = 'site_content.delete_photo'
    template_name = 'site_content/photo_delete.html'
    success_message = 'Photo deleted successfully'
    success_url = '/gallery/'

class PhotoEditView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """View for editing gallery photos"""
    model = Photo
    permission_required = 'site_content.delete_photo'
    fields = ['title', 'photo_full', 'photo_thumbnail', 'categories']
    template_name = 'site_content/photo_upload.html'
    success_message = 'Photo edited succesfully'
    success_url = '/gallery/'
