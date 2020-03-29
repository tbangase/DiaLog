from django import forms
from .models import User, Diary

class DiaryForm(forms.ModelForm):
  class Meta:
    model = Diary
    fields = ['title', 'content']
    title = forms.CharField(
      label="title", max_length=200, 
      required=True, widget = forms.TextInput()
    )
    content = forms.CharField(
      label="content", max_length=2000,
      required=True)
    #fields = ('title', 'content')
    labels = {
      'title': 'タイトル',
      'content': '日記'
    }
    help.texts = {
      'title': '日記のまとめを一行で表現してください',
      'content': 'こちらに日記をお書きください'
    }

    widgets = {
      'content': forms.Textarea(attrs={'rows':6,'cols':15}),
    }
