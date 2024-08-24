from django.urls import path
from .views import index, add_teacher, edit_teacher

app_name = 'teacher'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_teacher, name='add'),
    path('edit/', edit_teacher, name='edit'),
]