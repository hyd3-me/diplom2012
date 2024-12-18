from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class GroupTest(TestCase):

    def test_check_pwd_for_group(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, group = utils.check_pwd4group(group, data.GROUP1[1])
        self.assertFalse(err)
    
    def test_check_wrong_pwd_for_group(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, group = utils.check_pwd4group(group, 'anyWrongPWD')
        self.assertTrue(err)
    
    def test_can_get_groups_by_user(self):
        err, user = utils.create_user(data.USER1)
        err, group_and_staff1 = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        err, group_and_staff2 = utils.create_group_and_staff(
            data.GROUP2[0], data.GROUP2[1], user)
        err, query_set_groups = utils.get_qs_groups_by_user(user)
        self.assertFalse(err)
        self.assertIn(group_and_staff1[0], query_set_groups)
        self.assertIn(group_and_staff2[0], query_set_groups)

class StaffTest(TestCase):

    def test_can_create_staff(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, staff = utils.create_staff(group, user)
        self.assertFalse(err)
    
    def test_can_get_staff_from_user(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, staff = utils.create_staff(group, user)
        err, q_staff_from_user = utils.get_staff_by_user(user)
        self.assertFalse(err)
        self.assertEqual(staff, q_staff_from_user[0])
    
    def test_has_owner_for_group(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        self.assertEqual(user, group.owner)
    
    def test_create_group_and_staff(self):
        err, user = utils.create_user(data.USER1)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        self.assertFalse(err)
    
    def test_owner_has_su_rank(self):
        err, user = utils.create_user(data.USER1)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        self.assertEqual(group_and_staff[1].rank, 7)
    
    def test_can_join_group(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, user2 = utils.create_user(data.USER2)
        err, staff = utils.join_group(group, user2)
        self.assertFalse(err)
        self.assertFalse(staff.rank)
    
    def test_can_get_group_by_name(self):
        err, user = utils.create_user(data.USER1)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user)
        err, group_by_name = utils.get_group_by_name(data.GROUP1[0])
        self.assertFalse(err)
        self.assertEqual(group, group_by_name)
    
    def test_can_get_group_from_staff(self):
        err, user = utils.create_user(data.USER1)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        err, group_from_staff = utils.get_group_from_staff(group_and_staff[1])
        self.assertFalse(err)
        self.assertEqual(group_and_staff[0], group_from_staff)
