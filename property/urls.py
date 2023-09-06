from django.urls import include, path
from .views import *
urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('create/', PropertyCreateView.as_view(), name='property-create'),
    path('detail/', PropertyDetailView.as_view(), name='property-detail'),

]