from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path(data.LOGIN_PATH,       views.login_view, name=data.LOGIN_PATH),
    path(data.HOME_PATH,        views.home_view, name=data.HOME_PATH),
    path(data.REGISTER_PATH,    views.reg_view, name=data.REGISTER_PATH),
    ]