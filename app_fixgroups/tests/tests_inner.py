from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class GroupTest(TestCase):

    def test_check_pwd_for_group(self):
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1])
        err, group = utils.check_pwd4group(group, data.GROUP1[1])
        self.assertFalse(err)
    
    def test_check_wrong_pwd_for_group(self):
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1])
        err, group = utils.check_pwd4group(group, 'anyWrongPWD')
        self.assertTrue(err)

class StaffTest(TestCase):

    def test_can_create_staff(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1])
        err, staff = utils.create_staff(group, user)
        self.assertFalse(err)