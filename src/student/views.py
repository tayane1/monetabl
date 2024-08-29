from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messages framework
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    numbers_students = students.count()
    context = {
        'students': students,
        'total': numbers_students
    }
    return render(request, 'student/index.html', context)

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "L'élève a été ajouté avec succès.")  # Success message
            return redirect('student:index')
        else:
            messages.error(request, "Erreur lors de l'ajout de l'élève. Veuillez corriger le formulaire.")  # Error message
            return render(request, 'student/add.html', {'form': student_form})
    
    student_form = StudentForm()
    context = {'form': student_form}
    return render(request, 'student/add.html', context)

def update(request, id):
    student = Student.objects.get(id = id)
    
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "L'élève a été modifié avec succès.")  # Success message
            return redirect('student:index')
        else:
            messages.error(request, "Erreur lors de la modification de l'élève. Veuillez corriger le formulaire.")  # Error message
            return render(request, 'student/add.html', {'form': student_form})
    
    student_form = StudentForm(instance=student)
    
    context = {
        'form': student_form,
        'title': "Modifier élève",
    }
    return render(request, 'student/add.html', context)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "L'élève a été supprimé avec succès.")  # Success message
    return redirect('student:index')
