from django.test import TestCase
from django.urls import reverse
from unittest import skip

from proj_fix import proj_data as data, template_name as template


class BaseUser(TestCase):
    pass

class UserTest(BaseUser):

    def test_has_login_page(self):
        response = self.client.get(reverse(data.LOGIN_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.LOGIN_HTML)
    
    def test_redirect_from_home_page_to_login(self):
        # test redirect for not auth users
        response = self.client.get(reverse(data.HOME_PATH))
        self.assertRedirects(response, reverse(data.LOGIN_PATH))
        
    def test_has_link_to_create_user(self):
        response = self.client.get(reverse(data.LOGIN_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, '<a href="/register">new+</a>', html=True)
