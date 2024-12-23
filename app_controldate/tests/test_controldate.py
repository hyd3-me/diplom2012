from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser
from app_controldate import forms


class TestControlDate(BaseUser):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.login(data.USER1)
        self.user = user
    
    def test_has_link_to_groups_page(self):
        response = self.client.get(reverse(data.PROFILE_PATH))
        self.assertContains(
                response, f'<a href="{reverse(data.CONTROLDATE_PATH)}">control date</a>', html=True)

    def test_can_get_controldate_page(self):
        response = self.client.get(reverse(data.CONTROLDATE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.CONTROLDATE_HTML)

    def test_has_link_to_adddate(self):
        response = self.client.get(reverse(data.CONTROLDATE_PATH))
        self.assertContains(
                response,
                f'<a href="{reverse(data.ADDDATE_PATH)}">add date</a>',
                html=True)

    def test_can_get_adddate_page(self):
        response = self.client.get(reverse(data.ADDDATE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.ADDDATE_HTML)

    def test_can_get_adddate_form(self):
        response = self.client.get(reverse(data.ADDDATE_PATH))
        self.assertIsInstance(response.context['form'], forms.ControlDateForm)

    def test_can_adddate(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, e_date = utils.now_plus_day(3)
        response = self.client.post(reverse(data.ADDDATE_PATH), {
            'name': data.GOOD1,
            'e_date': e_date
        }, follow=True)
        self.assertContains(response, data.DATE_ADDED, html=True)

    def test_has_link_to_adddate(self):
        response = self.client.get(reverse(data.CONTROLDATE_PATH))
        self.assertContains(
                response,
                f'<a href="{reverse(data.RECORDSDATE_PATH)}">my records</a>',
                html=True)

    def test_can_get_recordsdate_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        response = self.client.get(reverse(data.RECORDSDATE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.RECORDSDATE_HTML)
    
    def test_can_get_end_date_records_on_page(self):
        err, e_date = utils.now_plus_day(3)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, records = utils.adddate(
            data.GOOD1, e_date, group_and_staff[1], group_and_staff[0]
        )
        err, records2 = utils.adddate(
            data.GOOD2, e_date, group_and_staff[1], group_and_staff[0]
        )
        response = self.client.get(reverse(data.RECORDSDATE_PATH))
        self.assertContains(response, data.GOOD1, html=True)
        self.assertContains(response, data.GOOD2, html=True)
    
    def test_has_red_col_for_today_rec(self):
        err, e_date = utils.now_plus_day(0)
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, records = utils.adddate(
            data.GOOD1, e_date, group_and_staff[1], group_and_staff[0]
        )
        response = self.client.get(reverse(data.RECORDSDATE_PATH))
        span_tag_red_col = 'red_col'
        self.assertContains(response, span_tag_red_col)
