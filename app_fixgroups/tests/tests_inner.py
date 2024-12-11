from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class UserTest(TestCase):

    def test_check_pwd_for_group(self):
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1])
        err, group = utils.check_pwd4group(group, data.GROUP1[1])
        self.assertFalse(err)
