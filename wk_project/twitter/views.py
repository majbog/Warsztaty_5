from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

import datetime

# Create your views here.
from .forms import SignInForm, LogInForm, NewCommFrom
from .models import Message, Comment, Following


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
            user = authenticate(username=User.objects.get(email=email).username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                ctx = {
                    'form': form
                }
                return render(request, "login.html", ctx)


class AllMsgsView(View):
    def get(self, request):
        all_msgs = Message.objects.all().order_by('-date')
        ctx={
            'all_msgs': all_msgs
        }
        return render(request, "all_msgs.html", ctx)


class NewCommentView(View):
    def get(self, request, msg_id):
        current_user = request.user
        form = NewCommFrom(
            initial={
                'author': current_user,
                'date': datetime.datetime.now().strftime('%Y-%m-%d'),
                'reference': Message.objects.get(id=msg_id)
            }
        )
        msg = Message.objects.get(id=msg_id)
        ctx = {
            'form': form,
            'msg': msg
        }
        return render(request, 'new_comm_form.html', ctx)
    def post(self, request, msg_id):
        form = NewCommFrom(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            date = form.cleaned_data['date']
            Comment.objects.create(author=author, text=text, date=date, reference=Message.objects.get(id=msg_id))
            return redirect('main')


class FollowUserView(View):
    pass