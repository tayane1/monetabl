from django.urls import path
from .views import index, add_user, edit_user

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_user, name='add'),
    path('edit/', edit_user, name='edit'),
]