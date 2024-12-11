from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from unittest import skip

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class BaseUser(TestCase):

    def reg_me(self, user_tuple=data.USER1):
        response = self.client.post(reverse(data.REGISTER_PATH), {
            'username': user_tuple[0],
            'password1':user_tuple[1],
            'password2':user_tuple[1]}, follow=True)
        return response
    
    def login(self, user_tuple=data.USER1):
        response = self.client.post(reverse(data.LOGIN_PATH), {
            'username': user_tuple[0],
            'password': user_tuple[1]}, follow=True)
        return response
    
    def logout(self):
        response = self.client.get(reverse(data.LOGOUT_PATH), follow=True)
        return response




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
    
    def test_has_register_page(self):
        response = self.client.get(reverse(data.REGISTER_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.REGISTER_HTML)
    
    def test_can_get_register_form(self):
        response = self.client.get(reverse(data.REGISTER_PATH))
        self.assertIsInstance(response.context['form'], UserCreationForm)
    
    def test_can_register_user(self):
        response = self.reg_me(data.USER1)
        self.assertContains(response, data.PROFILE_CREATED)
        err, user = utils.get_user(1)
        self.assertFalse(err)
        self.assertEqual(user.username, data.USER1[0])
    
    def test_redirect_after_register_user(self):
        response = self.reg_me()
        self.assertRedirects(response, reverse(data.PROFILE_PATH))

    def test_can_login(self):
        err, user = utils.create_user(data.USER1)
        response = self.login(data.USER1)
        self.assertContains(response, data.SUCCESS_LOG)
    
    def test_can_logout(self):
        err, user = utils.create_user(data.USER1)
        self.login(data.USER1)
        response = self.logout()
        self.assertContains(response, data.SUCCESS_OUT)
    
    def test_has_link_to_login(self):
        response = self.client.get(reverse(data.REGISTER_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, '<a href="/login">login</a>', html=True)
