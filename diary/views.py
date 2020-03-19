from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
  #template = loader.get_template('diary/index.html')
  return render(request, 'diary/index.html')

# Create your views here.
