from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import User, Diary
from .forms import DiaryForm

def home(request):
  #template = loader.get_template('diary/index.html')
  return render(request, 'diary/home.html')

def about(request):
  return render(request, 'diary/about.html')

def writing(request):
  params = {'message':'', 'form': None}
  if request.method == 'POST':
    form = DiaryForm(request.POST)
    if form.is_valid():
      diary = form.save(commit = False)
      diary.created_at = timezone.now()
      diary.user = User.objects.get(id=1)
      diary.save()
      return redirect('/index')
    else:
      params['message'] = 'もう一度入力してください'
      params['form'] = form
  else:
    params['form'] = DiaryForm()
  return render(request, 'diary/writing.html', params)

def index(request):
  latest_diary_list = Diary.objects.order_by('-created_at')[:5]
  context = {
    'latest_diary_list': latest_diary_list,
  }
  return render(request,'diary/index.html', context)

def detail(request):

  return render(request, 'diary/detail.html')

def signup(request):
  return render(request, 'diary/signup.html')

def login(request):
  return render(request, 'diary/login.html')

#def contact(request):
#  return render(request, 'diary/contact.html')




