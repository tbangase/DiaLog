from django.utils import timezone

from django.test import TestCase
from django.urls import reverse

from .models import User, Diary
# Create your tests here.


class DiaryViewTests(TestCase):
  def setup(self):
    user = User.objects.create(
      name = "example", created_at=timezone.now(),
      updated_at=timezone.now()
    )
    user.save()

  def test_home_page_presence_true(self):
    """
    Home page can response.
    """
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "DiaLog")
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/home.html')

  def test_about_page_presence_true(self):
    """
    About page can response.
    """
    response = self.client.get(reverse('about'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/about.html')

  def test_index_page_presence_true(self):
    """
    index page should exists.
    """
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/index.html')

  def test_detail_page_presence_true(self):
    """
    detail page should exists.
    """
    response = self.client.get(reverse('detail'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/detail.html')

  def test_writing_page_presence_true(self):
    """
    writing page should exists.
    """
    response = self.client.get(reverse('writing'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/writing.html')

  def test_signup_page_presence_true(self):
    """
    signup page should exists.
    """
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'diary/base.html')
    self.assertTemplateUsed(response, 'diary/signup.html')


