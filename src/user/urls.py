from django.urls import path
from .views import index, add_user, update

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_user, name='add'),
    path('update/<int:id>/', update, name='update'),
    
]