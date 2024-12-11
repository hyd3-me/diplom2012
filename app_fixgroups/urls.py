from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path('',  views.groups_view, name=data.GROUPS_PATH),
    ]