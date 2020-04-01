from django.utils import timezone

from django.test import TestCase
from django.urls import reverse

from .models import User, Diary
# Create your tests here.


class DiaryHomeViewTests(TestCase):
  def setup(self):
    user = User.objects.create(
      name = "example", created_at=timezone.now(),
      updated_at=timezone.now()
    )
    user.save()

  def page_presencei_true(self):
    """
    Home page can response.
    """
    response = self.client.get(reverse('diary:home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "DiaLog")


