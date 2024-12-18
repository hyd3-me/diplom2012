from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class ControlDateTest(TestCase):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.user = user
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        self.group_and_staff = group_and_staff

    def test_can_adddate(self):
        err, e_date = utils.now_plus_day(3)
        err, records = utils.adddate(
            data.GOOD1, e_date, self.group_and_staff[1], self.group_and_staff[0]
        )
        self.assertFalse(err)
    
    def test_can_get_end_date_from_group(self):
        err, e_date = utils.now_plus_day(3)
        err, records = utils.adddate(
            data.GOOD1, e_date, self.group_and_staff[1], self.group_and_staff[0]
        )
        err, end_date_by_group = utils.get_end_date_by_group(self.group_and_staff[0])
        self.assertFalse(err)
        self.assertEqual(end_date_by_group.count(), 1)
        self.assertIn(records, end_date_by_group)
        err, records2 = utils.adddate(
            data.GOOD2, e_date, self.group_and_staff[1], self.group_and_staff[0]
        )
        err, end_date_by_group = utils.get_end_date_by_group(self.group_and_staff[0])
        self.assertFalse(err)
        self.assertIn(records2, end_date_by_group)
        self.assertEqual(end_date_by_group.count(), 2)