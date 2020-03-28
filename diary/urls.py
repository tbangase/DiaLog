from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('writing', views.writing, name='writing'),
  path('index', views.index, name='index'),
  path('detail',views.detail,name='detail'),
  path('signup', views.signup, name='signup'),
#  path('contact', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
