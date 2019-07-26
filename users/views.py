"""
View module for the users app
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def register(request):
    """
    Register new user view. The view is displaying a blank form for a GET request.
    If request  method is POST, the form gets checked. If it is valid it gets saved,
    otherwise it is sent back to the user
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Profile view. The view is displaying current profile for a GET request.
    If request  method is POST, the forms gets checked. If they are valid,
    they get saved, and the user gets redirected back to his profile
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def profile_detail(request, username):
    """
    Get the username passed to the view by the url
    and try to match it to a user profile.
    If no profile with such username found then raise an exception
    """
    details = get_object_or_404(Profile, user__username=username)
    return render(request, 'users/profile_detail.html', {'details': details})
