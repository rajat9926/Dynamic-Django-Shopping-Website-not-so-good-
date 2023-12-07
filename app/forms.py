from django import forms
from .models import Cart,CustomerInfo,Product,OrderPlaced
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User

class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    password2 = forms.CharField(label='Cnf Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','strip':False}))

class PassChangeForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    new_password1= forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    new_password2= forms.CharField(label='Cnf Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerInfo
        fields=['name','city','state','locality','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}),'zipcode':forms.NumberInput(attrs={'class':'form-control'}),'state':forms.Select(attrs={'class':'form-control'})}

class PassResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Email'}),required=True)

class SetNewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    new_password2 = forms.CharField(label='Cnf New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)