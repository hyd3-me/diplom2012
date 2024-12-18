from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path('',                views.groups_view, name=data.GROUPS_PATH),
    path(data.CREATE_GROUP_PATH, views.create_group_view, name=data.CREATE_GROUP_PATH),
    path(data.JOIN_GROUP_PATH,   views.join_group_view, name=data.JOIN_GROUP_PATH),
    path(f'{data.MYGROUP_PATH}/<int:pk>/',  views.mygroup_view, name=data.MYGROUP_PATH),
    ]