from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template
from .forms import GroupCreationForm

# Create your views here.


def groups_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.GROUPS_HTML)

def create_group_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        group_form = GroupCreationForm(request.POST)
        if group_form.is_valid():
            group = group_form.save()
            messages.success(request, f'{data.GROUP_CREATED}')
            return redirect(data.GROUPS_PATH)
        messages.error(request, f'{data.INVALID_FORM}')
    # create form for group
    else:
        group_form = GroupCreationForm()
    return render(request, template.CREATE_GROUP_HTML, {'form': group_form})
