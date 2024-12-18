from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template

# Create your views here.


def login_view(request):
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.HOME_PATH)
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            new_user = auth_form.get_user()
            login(request, new_user)
            messages.success(request, f'{data.SUCCESS_LOG}')
            return redirect(data.PROFILE_PATH)
        messages.error(request, f'form invalid. perhaps there is no such user')
    else:
        auth_form = AuthenticationForm()
    return render(request, template.LOGIN_HTML, {'form': auth_form})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.HOME_HTML)

def reg_view(request):
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.HOME_PATH)
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save()
            login(request, new_user)
            messages.success(request, f'{data.PROFILE_CREATED}')
            return redirect(data.PROFILE_PATH)
        messages.error(request, f'{data.INVALID_FORM}')
    else:
        reg_form = UserCreationForm()
    return render(request, template.REGISTER_HTML, {'form': reg_form})

def profile_view(request):
    if not request.method == 'GET':
        return redirect(data.HOME_PATH)
    return render(request, template.PROFILE_HTML)

def logout_view(request):
    if not request.method == 'GET':
        return redirect(data.HOME_PATH)
    logout(request)
    messages.success(request, f'{data.SUCCESS_OUT}')
    return redirect(data.LOGIN_PATH)
