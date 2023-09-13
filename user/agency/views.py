from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from ..models import User
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login


class CreationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/agency_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agency'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')  # later on redirect will be dashboard

    def form_invalid(self, form):
        print("Your form is not valid")
        return redirect('agency-register')
