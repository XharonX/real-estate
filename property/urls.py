


from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import *
urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('new-property/', login_required(PropertyCreateView.as_view(), login_url='login'), name='property-create'),
    path('detail/<int:pk>', PropertyDetailView.as_view(), name='property-detail'),

]