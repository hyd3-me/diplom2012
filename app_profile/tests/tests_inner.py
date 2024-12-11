from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class UserTest(TestCase):

    def test_create_user(self):
        err, user = utils.create_user(data.USER1)
        self.assertFalse(err)
        self.assertEqual(user.username, data.USER1[0])
