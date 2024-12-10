from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path(data.LOGIN_PATH,       views.login_view, name=data.LOGIN_PATH),
    path(data.HOME_PATH,        views.home_view, name=data.HOME_PATH),
    path(data.REGISTER_PATH,    views.reg_view, name=data.REGISTER_PATH),
    path(data.PROFILE_PATH,     views.profile_view, name=data.PROFILE_PATH),
    path(data.LOGOUT_PATH,      views.logout_view, name=data.LOGOUT_PATH),
    ]