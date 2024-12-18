from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from proj_fix import proj_data as data, template_name as template
from app_profile import utils
from .forms import CreateRevisionForm

# Create your views here.


def revision_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        return redirect(data.ABOUT_PATH)
    return render(request, template.REVISION_HTML)

def create_revision_view(request, pk):
    if not request.user.is_authenticated:
        return redirect(data.LOGIN_PATH)
    if not request.method == 'GET':
        if not request.method == 'POST':
            return redirect(data.PROFILE_PATH)
        pass
    # create form for group
    else:
        revision_form = CreateRevisionForm()
    return render(request, template.CREATEREVISION_HTML, {'form': revision_form})