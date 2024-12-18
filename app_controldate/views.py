from django.shortcuts import render, redirect
from django.contrib import messages

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
            err, staff = utils.get_staff_by_user(request.user)
            if not err:
                err, group = utils.get_group_from_staff(staff[0])
                err, date_record_obj = utils.adddate(
                    adddate_form.cleaned_data.get('name'),
                    adddate_form.cleaned_data.get('e_date'),
                    staff[0],
                    group)
                if not err:
                    messages.success(request, f'{data.DATE_ADDED}')
                    return redirect(data.CONTROLDATE_PATH)
                else:
                    messages.error(request, f'{data.ADDDATE_ERROR}')
            else:
                messages.error(request, f'{data.NOT_STAFF_ERROR}')
        else:
            messages.error(request, f'{data.INVALID_FORM}')
    # create form for group
    else:
        adddate_form = ControlDateForm()
    return render(request, template.ADDDATE_HTML, {'form': adddate_form})

def recordsdate_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    err, staff = utils.get_staff_by_user(request.user)
    err, group = utils.get_group_from_staff(staff[0])
    err, end_date_list = utils.get_end_date_by_group(group)
    return render(request, template.RECORDSDATE_HTML, {'end_date_list': end_date_list})