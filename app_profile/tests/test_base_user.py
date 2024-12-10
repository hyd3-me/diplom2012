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
