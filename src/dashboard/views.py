from django.shortcuts import render


# Create your views here.

def index(request):
    
    return render(request,'index.html')

def home(request):

    context = {
        'student_count': 128100,
        'teacher_count': 1200,
        'user_count': 5000,
        'gender_distribution': [60, 40], 
    }
    return render(request, 'dashboard/home.html', context)