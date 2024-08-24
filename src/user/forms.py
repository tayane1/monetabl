from django import forms

class LoginForm(forms.Form):
    pseudo = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    