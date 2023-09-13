from django.urls import path
from .agency.views import CreationView as agency
from .owner.views import CreationView as owner
from .client.views import CreationView as client
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/agency/', agency.as_view(), name='agency-register'),
    path('signup/owner/', owner.as_view(), name='owner-register'),
    path('signup/user/', client.as_view(), name='client-register'),
    path('dashboard/<int:id>', Dashboard.as_view(), name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]