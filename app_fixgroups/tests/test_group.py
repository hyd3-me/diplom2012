from django.test import TestCase
from django.urls import reverse

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from app_profile.tests.test_base_user import BaseUser
from app_fixgroups import forms


class GroupTest(BaseUser):

    def setUp(self):
        err, user = utils.create_user(data.USER1)
        self.login(data.USER1)
        self.user = user
    
    def test_has_link_to_groups_page(self):
        response = self.client.get(reverse(data.PROFILE_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, f'<a href="{reverse(data.GROUPS_PATH)}">groups</a>', html=True)
    
    def test_can_get_groups_page(self):
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.GROUPS_HTML)
    
    def test_visit_only_auth_users(self):
        self.logout()
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertRedirects(response, reverse(data.LOGIN_PATH))
    
    def test_has_link_to_create_group(self):
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response,
                f'<a href="{reverse(data.CREATE_GROUP_PATH)}">create group</a>',
                html=True)
    
    def test_can_get_create_group_page(self):
        response = self.client.get(reverse(data.CREATE_GROUP_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.CREATE_GROUP_HTML)
    
    def test_can_get_create_group_form(self):
        response = self.client.get(reverse(data.CREATE_GROUP_PATH))
        self.assertIsInstance(response.context['form'], forms.GroupCreationForm)
    
    def test_create_group_HTML_conain_form(self):
        response = self.client.get(reverse(data.CREATE_GROUP_PATH))
        form = forms.GroupCreationForm()
        self.assertContains(response, form.as_p(), html=True)
    
    def test_can_create_group(self):
        response = self.client.post(reverse(data.CREATE_GROUP_PATH), {
            'name': data.GROUP1[0],
            'group_pwd': data.GROUP1[1]
        }, follow=True)
        self.assertContains(response, data.GROUP_CREATED, html=True)
    
    def test_has_link_to_join_group(self):
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response,
                f'<a href="{reverse(data.JOIN_GROUP_PATH)}">join group</a>',
                html=True)

    def test_can_get_join_group_page(self):
        response = self.client.get(reverse(data.JOIN_GROUP_PATH))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template.JOIN_GROUP_HTML)

    def test_join_group_HTML_contain_form(self):
        response = self.client.get(reverse(data.JOIN_GROUP_PATH))
        form = forms.GroupForm()
        self.assertContains(response, form.as_p(), html=True)
    
    def test_can_join_to_group(self):
        err, user2 = utils.create_user(data.USER2)
        err, group = utils.create_group(data.GROUP1[0], data.GROUP1[1], user2)
        response = self.client.post(reverse(data.JOIN_GROUP_PATH), {
            'name': data.GROUP1[0],
            'group_pwd': data.GROUP1[1]
        }, follow=True)
        self.assertContains(response, data.SUCCESS_JOIN_TO_GROUP, html=True)

    def test_can_view_my_groups(self):
        err, group_and_staff1 = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        err, group_and_staff2 = utils.create_group_and_staff(
            data.GROUP2[0], data.GROUP2[1], self.user)
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertContains(response, data.GROUP1[0], html=True)
        self.assertContains(response, data.GROUP2[0], html=True)
    
    def test_has_link_to_my_group(self):
        err, group_and_staff = utils.create_group_and_staff(
            data.GROUP1[0], data.GROUP1[1], self.user)
        response = self.client.get(reverse(data.GROUPS_PATH))
        self.assertContains(
                response, f'<a href="{reverse(data.MYGROUP_PATH, args=[group_and_staff[0].pk])}">{group_and_staff[0].name}</a>', html=True)
