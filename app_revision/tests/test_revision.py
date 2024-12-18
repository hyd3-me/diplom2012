from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser
from app_revision import forms


class TestRevision(BaseUser):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.user = user
        self.login(data.USER1)
    
    def test_has_link_for_create_revision(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        response = self.client.get(reverse(data.MYGROUP_PATH, args=[group_and_staff[0].pk]))
        self.assertContains(
            response, f'<a href="{reverse(data.CREATE_REVISION_PATH, args=[group_and_staff[0].pk])}">create revision</a>', html=True)
    
    def test_can_get_create_revision_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        response = self.client.get(reverse(data.CREATE_REVISION_PATH, args=[group_and_staff[0].pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.CREATEREVISION_HTML)

    def test_create_revision_HTML_contain_form(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        response = self.client.get(reverse(data.CREATE_REVISION_PATH, args=[group_and_staff[0].pk]))
        form = forms.CreateRevisionForm()
        self.assertContains(response, form.as_p(), html=True)
    
    def test_can_create_revision_via_http(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        url = reverse(data.CREATE_REVISION_PATH, args=[group_and_staff[0].pk])
        response = self.client.post(url, {
            'name': utils.get_today(), }, follow=True)
        self.assertRedirects(response, reverse(data.MYGROUP_PATH, args=[group_and_staff[0].pk]))
    
    def test_can_get_list_created_revision(self):
        err, self.group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        response = self.client.get(reverse(data.MYGROUP_PATH, args=[self.group_and_staff[0].pk]))
        self.assertContains(response, revision.name)
    
    def test_can_get_revision_id_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        response = self.client.get(reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.REVISION_HTML)
    
    def test_has_link_to_create_list(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        response = self.client.get(reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertContains(response,  f'<a href="{reverse(data.CREATE_LIST_PATH, args=[revision.pk])}">create list</a>', html=True)
    
    def test_can_get_create_list_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        response = self.client.get(reverse(data.CREATE_LIST_PATH, args=[revision.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.CREATE_LIST_HTML)
    
    def test_create_list_HTML_contain_form(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        response = self.client.get(reverse(data.CREATE_LIST_PATH, args=[revision.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], forms.CreateListForm)
        form = forms.CreateListForm()
        self.assertContains(response, form.as_p(), html=True)
    
    def test_can_create_list_via_http(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        url = reverse(data.CREATE_LIST_PATH, args=[revision.pk])
        response = self.client.post(url, {'name': data.LIST1, }, follow=True)
        self.assertRedirects(response, reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertContains(response, data.LIST_CREATED_SUCCESS)
    
    def test_can_get_created_lists_on_revision_page(self):
        err, self.group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list1 = utils.create_list(data.LIST1, revision)
        err, _list2 = utils.create_list(data.LIST2, revision)
        response = self.client.get(reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertContains(response, _list1.name)
    
    def test_can_get_list_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        response = self.client.get(reverse(data.LIST_PATH, args=[list_.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.LIST_HTML)
    
    def test_has_link_to_create_record(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        response = self.client.get(reverse(data.LIST_PATH, args=[list_.pk]))
        self.assertContains(response,  f'<a href="{reverse(data.CREATE_RECORD_PATH, args=[list_.pk])}">create record</a>', html=True)

    def test_can_get_create_record_page(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        url = reverse(data.CREATE_RECORD_PATH, args=[list_.pk])
        response = self.client.get(url, args=[list_.pk])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.CREATE_RECORD_HTML)

    def test_create_record_page_contain_form(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        err, list_ = utils.create_list(data.LIST1, revision)
        url = reverse(data.CREATE_RECORD_PATH, args=[list_.pk])
        response = self.client.get(url, args=[list_.pk])
        self.assertIsInstance(response.context['form'], forms.CreateRecordForm)
        form = forms.CreateRecordForm()
        self.assertContains(response, form.as_p(), html=True)
    
    def test_can_create_record_via_http(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        err, _list = utils.create_list(data.LIST1, revision)
        url = reverse(data.CREATE_RECORD_PATH, args=[_list.pk])
        response = self.client.get(url, args=[_list.pk])
        url = reverse(data.CREATE_RECORD_PATH, args=[_list.pk])
        response = self.client.post(url, {
            'name': data.RECORD1,
            'barcode': data.BARCODE1,
            'count': data.GOOD_COUNT1,
            'note': data.TEST_NOTE1,
            }, follow=True)
        self.assertRedirects(response, reverse(data.CREATE_RECORD_PATH, args=[_list.pk]))
        self.assertContains(response, data.CREATE_RECORD_SUCCESS)
    
    def test_can_get_created_record_on_list_page(self):
        err, self.group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list1 = utils.create_list(data.LIST1, revision)
        err, record1 = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, _list1, self.group_and_staff[1])
        err, record2 = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, _list1, self.group_and_staff[1])
        err, record3 = utils.create_record(data.RECORD2, data.BARCODE2, data.GOOD_COUNT1, data.TEST_NOTE1, _list1, self.group_and_staff[1])
        response = self.client.get(reverse(data.LIST_PATH, args=[_list1.pk]))
        self.assertContains(response, record1.name)
        self.assertContains(response, record2.name)
        self.assertContains(response, record3.name)
    
    def test_revision_page_has_form_for_search_record(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        response = self.client.get(reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertIsInstance(response.context['form'], forms.SearchRecordForm)
    
    def test_can_get_records_by_barcode_from_revision(self):
        err, self.group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, self.group_and_staff[0])
        err, _list1 = utils.create_list(data.LIST1, revision)
        err, _list2 = utils.create_list(data.LIST2, revision)
        err, record1 = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, _list1, self.group_and_staff[1])
        err, record2 = utils.create_record(data.RECORD1, data.BARCODE1, data.GOOD_COUNT1, data.TEST_NOTE1, _list2, self.group_and_staff[1])
        err, record3 = utils.create_record(data.RECORD2, data.BARCODE2, data.GOOD_COUNT1, data.TEST_NOTE1, _list2, self.group_and_staff[1])
        url = reverse(data.SEARCH_RECORD_PATH) + f'?revision_id={revision.pk}&barcode={data.BARCODE1}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.SEARCH_RECORD_HTML)
        self.assertContains(response, record1.name)
        self.assertContains(response, _list1.name)
        self.assertContains(response, _list2.name)
