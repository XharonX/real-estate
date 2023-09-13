from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from ..models import User
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login


class CreationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/client_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def form_invalid(self, form):
        print("Ur form is invalid")
        return redirect('client-register')
