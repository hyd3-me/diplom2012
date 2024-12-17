from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser


class TestControlDate(BaseUser):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.login(data.USER1)
        self.user = user
    
    def test_has_link_to_groups_page(self):
        response = self.client.get(reverse(data.PROFILE_PATH))
        self.assertContains(
                response, f'<a href="{reverse(data.CONTROLDATE_PATH)}">control date</a>', html=True)
    