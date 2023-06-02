from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import *


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
        return render(request, 'users/login.html', {'form': form})


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'users/signin.html', {'form' : form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:login')  # Перенаправление на главную страницу
        return render(request, 'users/signin.html', {'form': form})