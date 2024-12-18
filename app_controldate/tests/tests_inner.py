from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class ControlDateTest(TestCase):

    def test_can_adddate(self):
        err, user = utils.create_user(data.USER1)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        err, e_date = utils.now_plus_day(3)
        err, records = utils.adddate(
            data.GOOD1, e_date, group_and_staff[1], group_and_staff[0]
        )
        self.assertFalse(err)