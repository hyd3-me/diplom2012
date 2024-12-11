from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser


class GroupTest(BaseUser):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.login(data.USER1)
        self.user = user
    
    def test_has_link_to_groups_page(self):
        response = self.client.get(reverse(data.PROFILE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, f'<a href="{reverse(data.GROUPS_PATH)}">groups</a>', html=True)
    
    def test_can_get_groups_page(self):
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.GROUPS_HTML)
    
    def test_visit_only_auth_users(self):
        self.logout()
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertRedirects(response, reverse(data.LOGIN_PATH))