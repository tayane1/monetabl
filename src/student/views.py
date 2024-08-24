from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'student/index.html')

def add_student(request):

    form = StudentForm()
    
    context = {'form': form}
    
    return render(request, 'student/add.html', context)

def edit_student(request):
    
    return render(request, 'student/edit.html')
