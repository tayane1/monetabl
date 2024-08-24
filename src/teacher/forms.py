from django import forms

class TeacherForm(forms.Form):
    lastName = forms.CharField(max_length=50)
    firstName = forms.CharField(max_length=50)
    birthDay = forms.DateField()
    city = forms.CharField(max_length=100)
    telephon = forms.CharField(max_length=15)