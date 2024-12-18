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