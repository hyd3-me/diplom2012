from django.test import TestCase

from proj_fix import proj_data as data, template_name as template
from app_profile import utils


class RevisionTest(TestCase):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.user = user
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], user)
        self.group_and_staff = group_and_staff
    
    def test_can_create_revision(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        self.assertFalse(err)
        self.assertEqual(revision.name, today)
    
    def test_can_create_list(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        self.assertFalse(err)
        self.assertEqual(list_.name, data.LIST1)
    
    def test_can_create_record(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        err, record = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, list_, self.group_and_staff[1])
        self.assertFalse(err)
    
    def test_can_get_list_by_id(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list = utils.create_list(data.LIST1, revision)
        err, _list_from_db = utils.get_list_by_id(_list.pk)
        self.assertFalse(err)
        self.assertEqual(_list, _list_from_db)
    
    def test_can_get_all_list_from_revision(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list1 = utils.create_list(data.LIST1, revision)
        err, _list2 = utils.create_list(data.LIST2, revision)
        err, qs_lists = utils.get_all_lists_from_revision(revision)
        self.assertFalse(err)
        self.assertEqual(qs_lists.count(), 2)
        self.assertIn(_list1, qs_lists)
        self.assertIn(_list2, qs_lists)
    
    def test_can_get_all_records_from_list(self):
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list = utils.create_list(data.LIST1, revision)
        err, record1 = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, _list, self.group_and_staff[1])
        err, record2 = utils.create_record(data.RECORD2, data.BARCODE2, data.GOOD_COUNT1, data.TEST_NOTE1, _list, self.group_and_staff[1])
        err, qs_records = utils.get_all_records_from_list(_list)
        self.assertFalse(err)
        self.assertEqual(qs_records.count(), 2)
        self.assertIn(record1, qs_records)
        self.assertIn(record2, qs_records)
