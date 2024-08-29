from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer le nom de l\'élève' }),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer le prénom de l\'élève' }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthDay': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer la date de naissance de l\'élève'}),
            'telephon': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Entrer le numéro de téléphone de l\'élève'}),
            'classRoom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer la classe de l\'élève'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer le matricule'}),
        }


    
    