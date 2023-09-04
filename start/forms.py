from django import forms
from django.forms import ModelForm, fields, widgets
from django.forms import TextInput, EmailInput, FileInput, Select, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Followers

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField(max_length=50, help_text='first_name')
    last_name = forms.CharField(max_length=50, help_text='last_name')
    email = forms.EmailField(max_length=50, help_text='email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


def save(self, commit=True):
    user = super(RegisterForm, self).save(commit = False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user

class UserProfileForm (forms.ModelForm):
    dob = forms.DateField(required=True)

    class Meta:
        model = UserProfile
        fields = ('dob',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
        # widgets = {
        #     'username': TextInput(attrs={'class': 'input', 'placeholder': 'User Name'}),
        #     'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
        #     'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
        #     'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
        # }

class ProfileUpdateForm1(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob', 'image')
        # widgets = {
        #     'dob': DateInput(attrs={'class': 'input', 'placeholder': 'mm/dd/yyyy'}),
        #     'image': FileInput(attrs={'placeholder': 'Profile Photo'}),
        # }

class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = ('followed', 'follower')