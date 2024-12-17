from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from .forms import ControlDateForm

# Create your views here.


def controldate_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.CONTROLDATE_HTML)

def adddate_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        adddate_form = ControlDateForm(request.POST)
        if adddate_form.is_valid():
            err, group_and_staff = utils.create_group_and_staff(
                adddate_form.cleaned_data.get('name'),
                adddate_form.cleaned_data.get('group_pwd'),
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
        adddate_form = ControlDateForm()
    return render(request, template.ADDDATE_HTML, {'form': adddate_form})