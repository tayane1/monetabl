from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserForm
from.models import User

# Create your views here.

def index(request):
    
    users = User.objects.all()
    numbers_users = users.count()
    context = {
        'users': users,
        'total' : numbers_users
    }

    return render(request, 'user/index.html', context)
    
def add_user(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_form.save()
            messages.success(request, "L'utilisateur a été ajouter avec succès.")
            return redirect('user:index')
        else:
            messages.error(request, "Erreur lors de l'ajout de l'utilisateur. Veuillez corriger le formulaire.")
            return render(request, 'user/add.html')
    
    user_form = UserForm()
    
    context = {'form': user_form}
    
    return render(request, 'user/add.html', context)

def update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "L'utilisateur a été modifié avec succès.")  # Success message
            return redirect('user:index')
        else:
            messages.error(request, "Erreur lors de la modification de l'utilisateur. Veuillez corriger le formulaire.")  # Error message
            return render(request, 'user/add.html', {'form': user_form})
    
    user_form = UserForm(instance=user)
    context = {
        'form': user_form,
        'title': "Modifier utilisateur",
    }
    return render(request, 'user/add.html', context)
