from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['lastName', 'firstName', 'birthDay', 'city', 'telephon', 'vacant', 'subjectSign', 'nextCours', 'topicNextMeeting']
        widgets = {
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre Nom'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre Prénom'}),
            'birthDay': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre Ville'}),
            'telephon': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre numéro'}),
        }
