from django.urls import path
from .views import index, add_student, edit_student

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_student, name='add'),
    path('edit/', edit_student, name='edit'),
]
