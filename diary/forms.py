from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Diary

class UserSignupForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  class Meta:
    model   = User
    fields  = ("email", "password1", "password2",)

class UserLoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  
  class Meta:
    model   = User
    fields  = ("username", "password",)

class DiaryForm(forms.ModelForm):
  class Meta:
    model   = Diary
    fields  = ['title', 'content']
    title   = forms.CharField(
      label="title", max_length=200, 
      required=True, widget=forms.TextInput()
    )
    content = forms.CharField(
      label="content", max_length=2000,
      required=True)
    #fields = ('title', 'content')
    labels  = {
      'title': 'タイトル',
      'content': '日記'
    }
    help.texts = {
      'title': '日記のまとめを一行で表現してください',
      'content': 'こちらに日記をお書きください'
    }

    widgets = {
      'content': forms.Textarea(attrs={'rows':4,'cols':15}),
    }

