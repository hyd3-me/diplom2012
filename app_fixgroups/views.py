from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template
from .forms import GroupCreationForm, GroupForm
from app_profile import utils

# Create your views here.


def groups_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    err, groups = utils.get_qs_groups_by_user(request.user)
    return render(request, template.GROUPS_HTML, {'groups': groups})

def create_group_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        group_form = GroupCreationForm(request.POST)
        if group_form.is_valid():
            err, group_and_staff = utils.create_group_and_staff(
                group_form.cleaned_data.get('name'),
                group_form.cleaned_data.get('group_pwd'),
                request.user)
            if not err:
                messages.success(request, f'{data.GROUP_CREATED}')
                return redirect(data.GROUPS_PATH)
            else:
                messages.error(request, f'{data.GROUP_CREATION_ERR}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    # create form for group
    else:
        group_form = GroupCreationForm()
    return render(request, template.CREATE_GROUP_HTML, {'form': group_form})

def join_group_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            err, group = utils.get_group_by_name(
                group_form.cleaned_data.get('name'))
            if err or (not group):
                messages.error(request, f'error receiving the group')
            else:
                err, state = utils.check_pwd4group(
                    group, group_form.cleaned_data.get('group_pwd'))
                if err:
                    messages.error(request, f'invalid password')
                else:
                    err, staff = utils.join_group(group, request.user)
                    if not err:
                        messages.success(request, f'{data.SUCCESS_JOIN_TO_GROUP}')
                        return redirect(data.GROUPS_PATH)
                    messages.error(request, f'{data.FAILED_JOIN_TO_GROUP}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    # create form for group
    else:
        group_form = GroupForm()
    return render(request, template.JOIN_GROUP_HTML, {'form': group_form})

def mygroup_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    err, group = utils.get_group_by_id(pk)
    err, qs_revisions = utils.get_all_revisions_from_group(group)
    return render(request, template.MYGROUP_HTML, {'group_id': pk, 'qs_revisions': qs_revisions})