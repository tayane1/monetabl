from django.shortcuts import render
from .forms import TeacherForm

# Create your views here.

def index(request):

    return render(request, 'teacher/index.html')


def add_teacher(request):
    
    form = TeacherForm()
    context = {'form': form}
    
    return render(request, 'teacher/add.html', context)


def edit_teacher(request):
    return render(request, 'teacher/edit.html')