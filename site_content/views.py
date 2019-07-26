from django.shortcuts import render

def index(request):
    return render(request, 'site_content/index.html')

def gallery(request):
    return render(request, 'site_content/gallery.html')

def services(request):
    return render(request, 'site_content/services.html')

def contact(request):
    return render(request, 'site_content/contact.html')
