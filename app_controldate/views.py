from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template
from app_profile import utils

# Create your views here.


def controldate_view(request):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.CONTROLDATE_HTML)