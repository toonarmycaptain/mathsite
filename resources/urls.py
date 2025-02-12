from django.urls import path
from django.views import generic
from . import views
from . import models

urlpatterns = [
    path("resources", views.all_resources, name="all_resources"),
    path("edit_resource/<int:id>", views.edit_resource, name="edit_resource"),
    path("view_resource/<int:id>", views.view_resource, name="view_resource"),
    path("update_resource/<int:id>", views.update_resource, name="update_resource"),
    path("delete_resource/<int:id>", views.delete_resource, name="delete_resource"),
    path(
        "create_resource",
        generic.TemplateView.as_view(template_name="resources/create_resource.html"),
        name="create_resource",
    ),
    path("save_new_resource", views.save_new_resource, name="save_new_resource"),
    path(
        "resource_list",
        generic.ListView.as_view(
            model=models.Resource,
        ),
    ),
]
