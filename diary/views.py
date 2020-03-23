from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def home(request):
  #template = loader.get_template('diary/index.html')
  return render(request, 'diary/home.html')

def about(request):
  return render(request, 'diary/about.html')

def writing(request):
  return render(request, 'diary/writing.html')

def index(request):
  return render(request, 'diary/index.html')

def contact(request):
  return render(request, 'diary/contact.html')




