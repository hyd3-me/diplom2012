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
    
    def test_can_create_list_via_http(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, today = utils.get_today()
        err, revision = utils.create_revision(today, group_and_staff[0])
        url = reverse(data.CREATE_LIST_PATH, args=[revision.pk])
        response = self.client.post(url, {'name': data.LIST1, }, follow=True)
        self.assertRedirects(response, reverse(data.REVISION_PATH, args=[revision.pk]))
        self.assertContains(response, data.LIST_CREATED_SUCCESS)