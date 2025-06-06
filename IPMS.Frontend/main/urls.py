from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/get_minimum_variance', views.get_minimum_variance, name='get_minimum_variance'),
]