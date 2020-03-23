from django.db import models

# Create your models here.

class User(models.Model):
  name        = models.CharField(max_length=100)
  created_at  = models.DateTimeField('user created')
  updated_at  = models.DateTimeField('user updated')
  level       = models.IntegerField(default=0)
  exp         = models.IntegerField(default=0)
  
  def __str__(self):
    return self.name


class Diary(models.Model):
  user        = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at  = models.DateTimeField('diary created')
  title       = models.CharField(max_length= 200, default="")
  content     = models.CharField(max_length= 2000)

  def __str__(self):
    return self.content

