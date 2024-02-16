# applerestore/auth_app/views.py

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (CustomUserCreationForm, ConfirmPasswordForm, UsernameChangeForm,)

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('dashboard') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth_app/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Неправильное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

@login_required 
def dashboard(request):
    return render(request, 'auth_app/dashboard.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Ваш пароль был успешно обновлен!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth_app/change_password.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        form = ConfirmPasswordForm(request.user, request.POST)
        if form.is_valid():
            request.user.delete()  # Удаление пользователя
            messages.success(request, 'Ваш профиль был удален.')
            return redirect('home')
        else:
            messages.error(request, 'Неправильный пароль.')
    else:
        form = ConfirmPasswordForm(request.user)
    return render(request, 'auth_app/delete_profile.html', {'form': form})

@login_required
def change_username(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше имя пользователя было успешно изменено.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = UsernameChangeForm(instance=request.user)
    return render(request, 'auth_app/change_username.html', {'form': form})
