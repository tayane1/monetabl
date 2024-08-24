from django.urls import path
from .views import index, home

app_name = 'dashboard'


urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
]