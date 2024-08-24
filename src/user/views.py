from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'user/index.html')
    
def add_user(request):
    
    form = LoginForm()
    
    context = {'form': form}
    
    return render(request, 'user/add.html', context)

def edit_user(request):
    return render(request, 'user/edit.html')
