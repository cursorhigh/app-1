from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='email')

