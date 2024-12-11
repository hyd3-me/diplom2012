from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser


class GroupTest(BaseUser):
    
    def test_has_link_to_groups_page(self):
        response = self.client.get(reverse(data.PROFILE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, f'<a href="{reverse(data.GROUPS_PATH)}">groups</a>', html=True)