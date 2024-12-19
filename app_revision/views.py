from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from .forms import CreateRevisionForm, CreateListForm, CreateRecordForm

# Create your views here.


def revision_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.REVISION_HTML, {'revision_id': pk})

def create_revision_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        revision_form = CreateRevisionForm(request.POST)
        if revision_form.is_valid():
            err, group = utils.get_group_by_id(pk)
            if not err:
                err, revision = utils.create_revision(
                    revision_form.cleaned_data.get('name'), group)
                if not err:
                    messages.success(request, f'{data.CREATE_REVISION_SUCCESS}')
                    return redirect(reverse(data.MYGROUP_PATH, args=[pk]))
                else:
                    messages.error(request, f'{data.CREATE_REVISION_FAILED}')
            else:
                messages.error(request, f'{data.GROUP_NOT_FOUND}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    # create form for group
    else:
        revision_form = CreateRevisionForm()
    return render(request, template.CREATEREVISION_HTML, {'form': revision_form, 'group_id': pk})

def create_list_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        list_form = CreateListForm(request.POST)
        if list_form.is_valid():
            err, revision = utils.get_revision_by_id(pk)
            if not err:
                err, list_ = utils.create_list(list_form.cleaned_data.get('name'), revision)
                if not err:
                    messages.success(request, f'{data.LIST_CREATED_SUCCESS}')
                    return redirect(reverse(data.REVISION_PATH, args=[pk]))
                else:
                    messages.error(request, f'{data.CREATE_LIST_FAILED}')
            else:
                messages.error(request, f'{data.REVISION_NOT_FOUND}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    list_form = CreateListForm()
    return render(request, template.CREATE_LIST_HTML, {'form': list_form, 'revision_id': pk})

def list_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.LIST_HTML, {'list_id': pk})

def create_record_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        create_form = CreateRecordForm(request.POST)
        if create_form.is_valid():
            err, _list = utils.get_list_by_id(pk)
            if not err:
                err, staff = utils.get_staff_by_user(request.user)
                if not err:
                    err, record = utils.create_record(
                        create_form.cleaned_data.get('name'),
                        create_form.cleaned_data.get('barcode'),
                        create_form.cleaned_data.get('count'),
                        create_form.cleaned_data.get('note'),
                        _list,
                        staff[0],)
                    if not err:
                        messages.success(request, f'{data.CREATE_RECORD_SUCCESS}')
                        return (redirect(reverse(data.CREATE_RECORD_PATH, args=[pk])))
                    else:
                        messages.error(request, f'{data.CREATE_RECORD_FAILED}')
                else:
                    message.error(request, f'{data.STAFF_NOT_FOUND}')
            else:
                messages.error(request, f'{data.LIST_NOT_FOUND}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    record_form = CreateRecordForm()
    return render(request, template.CREATE_RECORD_HTML, {'form': record_form, 'list_id': pk})