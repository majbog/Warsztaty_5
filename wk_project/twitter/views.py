from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView

# Create your views here.
from .forms import SignInForm


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
            pass



class LogInView(View):
    pass
