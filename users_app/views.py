from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


# Create your views here.
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

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    model = User
    success_url = 'home'
    success_message = 'Logged in as %(username)s'