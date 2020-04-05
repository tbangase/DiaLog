from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic.base import View
from django.utils import timezone

from .models import User, Diary
from .forms import DiaryForm, UserSignupForm, UserLoginForm

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

#def contact(request):
#  return render(request, 'diary/contact.html')

class SignupAccount(CreateView):
  def post(self, request, *args, **kwargs):
    params = {'message':'', 'form': None}
    form = UserSignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit = False)
      user.username = form.fields.get('email')
      user.created_at = user.updated_at = timezone.now()
      user.save()
      username = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)
      params['form'] = form
      return redirect('/index')
    else:
      params['message'] = 'もう一度入力してください'
      params['form'] = form
    return render(request, 'diary/signup.html', params)

  def get(self, request, *args, **kwargs):
    form = UserSignupForm()
    return render(request, 'diary/signup.html', {'form': form,})

signup = SignupAccount.as_view()

class AccountLogin(View):
  def post(self, request, *arg, **kwargs):
    params = {'message':'', 'form': None}
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('email')
      user = User.objects.get(username=username)
      login(request, user)
      params['form'] = form
      return redirect('/index')
    else:
      params['message'] = 'もう一度入力してください'
      params['form']    = form
    return render(request, 'diary/login.html', params)

  def get(self, request, *args, **kwargs):
    form = UserLoginForm()
    return render(request, 'diary/login.html', {'form': form,})

login = AccountLogin.as_view()



