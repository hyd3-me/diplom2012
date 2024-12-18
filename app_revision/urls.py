from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path('',        views.revision_view, name=data.REVISION_PATH),
    ]