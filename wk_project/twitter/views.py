from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView

# Create your views here.
from .forms import SignInForm, LogInForm


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        ctx = {
            "form": form
        }
        return render(request, "auth/user_form.html", ctx)
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', "User with such mail is already registered")
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', "User with such login name already registered")
            if not form.errors:
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                User.objects.create_user(
                    username,
                    email,
                    password,
                    first_name=first_name,
                    last_name=last_name
                )
                return redirect("login")
        ctx = {
            "form": form
        }
        return render(request, "auth/user_form.html", ctx)



class LogInView(View):
    def get(self, request):
        form = LogInForm()
        ctx = {
            'form': form
        }
        return render(request, "login.html", ctx)

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=User.objects.get(email=email), password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return render(request, "login.html", ctx)


class AllOinksView(View):
    pass