from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def index(request):

    teachers = Teacher.objects.all()
    numbers_teachers = teachers.count()
    context = {
        'teachers': teachers,
        'total': numbers_teachers
    }

    return render(request, 'teacher/index.html', context)


def add_teacher(request):

    if request.method == 'POST':
        print(request.POST)
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            print(teacher_form.cleaned_data)
            teacher_form.save()
            messages.success(request, "Le professeur a été ajouter avec succès.")  # Success message
            return redirect('teacher:index')
        else:
            messages.error(request, "Erreur lors de l'ajout du professeur. Veuillez corriger le formulaire.")  # Error message
            return render(request, 'teacher/add.html')
    
    teacher_form = TeacherForm()
    context = {'form': teacher_form}
    
    return render(request, 'teacher/add.html', context)


def update(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            messages.success(request, "Le professeur a été modifié avec succès.")  # Success message
            return redirect('teacher:index')
        else:
            messages.error(request, "Erreur lors de la modification du professeur. Veuillez corriger le formulaire.")  # Error message
            return render(request, 'teacher/add.html', {'form': teacher_form})
    
    teacher_form = TeacherForm(instance=teacher)
    context = {
        'form': teacher_form,
        'title': "Modifier professeur",
    }
    return render(request, 'teacher/add.html', context)

def delete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    messages.success(request, "Le professeur a été supprimé avec succès.")  # Success message
    return redirect('teacher:index')
