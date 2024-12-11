from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class UserTest(TestCase):

    def test_create_user(self):
        err, user = utils.create_user(data.USER1)
        self.assertFalse(err)
        self.assertEqual(user.username, data.USER1[0])
    
    def test_can_get_all_user_from_db(self):
        # test empty db
        err, users = utils.get_all_users()
        self.assertFalse(err)
        self.assertEqual(len(users), 0)
        # create user and test equals to 1
        err, user = utils.create_user(data.USER1)
        err, users = utils.get_all_users()
        self.assertEqual(len(users), 1)
        err, user = utils.create_user(data.USER2)
        err, users = utils.get_all_users()
        self.assertEqual(len(users), 2)