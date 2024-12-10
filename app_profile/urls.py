from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path(data.LOGIN_PATH,   views.login_view, name=data.LOGIN_PATH),
    ]