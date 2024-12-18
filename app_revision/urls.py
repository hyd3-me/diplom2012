from django.urls import path, include, reverse
from . import views

from proj_fix import proj_data as data


urlpatterns = [
    path('<int:pk>/',        views.revision_view, name=data.REVISION_PATH),
    path(f'{data.CREATE_REVISION_PATH}/<int:pk>/', views.create_revision_view, name=data.CREATE_REVISION_PATH),
    path(f'{data.CREATE_LIST_PATH}/<int:pk>/', views.create_list_view, name=data.CREATE_LIST_PATH),
    ]