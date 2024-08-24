from django import forms

class StudentForm(forms.Form):
    lastName = forms.CharField(max_length=50)
    firstName = forms.CharField(max_length=50)
    birthDay = forms.DateField()
    