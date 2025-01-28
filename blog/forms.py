from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _  
from .models import Post

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})}

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autofocus':True,'auto-complete':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'title': 'Title', 'desc': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, user=None, commit=True):  # Accept user as an argument
        post = super().save(commit=False)
        if user:
            post.user_id = user.id  # Use user_id instead of author
        if commit:
            post.save()
        return post

