from django.test import TestCase
from django.urls import reverse
from unittest import skip


class UserTest(TestCase):

    def test_has_login_page(self):
        response = self.client.get(reverse(proj_data.LOGIN_PATH))
        self.assertEqual(response.status_code, 200)