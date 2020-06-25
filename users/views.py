from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "legendsd@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "legendsd@gmail.com"})
        return render(request, "users/login.html", {"form": form})


def login_view(request):
    if request.method == "GET":
        pass

    elif request.method == "POST":
        pass


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))
