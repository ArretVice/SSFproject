from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
import requests

from .models import Profile
from .forms import CustomUserCreationForm, UserForm, ProfileForm


# Create your views here.
class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    model = User
    success_url = 'home'
    success_message = 'Logged in as %(username)s'


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Account created! Logged in as {username}')
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/register.html', {'form': form})

@login_required(login_url='users:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

@login_required(login_url='users:login')
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users_app/edit_profile.html', {'form': user_form, 'profile_form': profile_form})

@login_required(login_url='users:login')
def delete_user(request):
    user = get_object_or_404(User, id=request.user.id)
    return render(request, 'users_app/delete_user.html', {'user': user})

@login_required(login_url='users:login')
def confirm_delete_user(request):
    user = get_object_or_404(User, id=request.user.id)
    user_name = user.username
    user.delete()
    messages.success(request, f'{user_name} deleted')
    return redirect('home')

def vk_view(request):
    access_token = request.user.social_auth.get(provider='vk-oauth2').extra_data.get('access_token')
    #access_token = request.user.social_auth.filter(provider='vk-oauth2')[0].extra_data.get('access_token')

    # getting your profile
    url = 'https://api.vk.com/method/'
    method = 'getProfiles'
    response = requests.get(url + method, params={'access_token': access_token, 'v': '5.21'})
    your_profile = response.json()['response'][0]
    your_profile = ' '.join((your_profile['first_name'], your_profile['last_name']))

    # getting your friendslist
    url = 'https://api.vk.com/method/'
    method = 'friends.get'
    response = requests.get(url + method, params={
        'access_token': access_token,
        'v': '5.21', 
        'order': 'random',
        'fields': ('first_name', 'last_name')
        })
    friends = response.json()['response']['items']
    friends = friends[:5] if len(friends) >= 5 else friends
    friends = [' '.join((user['first_name'], user['last_name'])) for user in friends]
    context = {'your_profile': your_profile, 'friends': friends}
    return render(request, 'users_app/vk_view.html', context)