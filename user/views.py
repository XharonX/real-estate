from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import *
from .client.forms import LoginForm
from django.views.generic import FormView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    return render(request, 'account/register.html')


class LoginView(FormView):
    form_class = LoginForm
    success_url = 'home'
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        form = request.POST
        username = form['username']
        password = form['password']
        if '@' in username:
            print()
            user = authenticate(request, email=username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            print('username and password are not match')
            return redirect('login')

class Dashboard(DetailView):
    pass