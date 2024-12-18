from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from .forms import CreateRevisionForm

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
        return redirect(data.ABOUT_PATH)
    return render(request, template.CREATE_LIST_HTML, {'revision_id': pk})