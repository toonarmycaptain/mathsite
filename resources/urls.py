from django.urls import path
from django.views import generic
from . import views
from . import models

urlpatterns = [
    path("resources", views.all_resources, name="all_resources"),
    path("view_resource/<int:id>", views.view_resource, name="view_resource"),
    path(
        "resourcesresource/update/<int:resource_id>/",
        views.update_resource,
        name="update_resource",
    ),
    path("delete_resource/<int:id>", views.delete_resource, name="delete_resource"),
    path(
        "resource/create/", views.create_resource, name="create_resource"
    ),  # Create resource
    path(
        "resource/update/<int:resource_id>/",
        views.update_resource,
        name="update_resource",
    ),  # Update resource
    path(
        "resource_list",
        generic.ListView.as_view(
            model=models.Resource,
        ),
    ),
]
