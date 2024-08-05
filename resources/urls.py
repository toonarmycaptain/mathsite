from django.urls import path
from . import views

urlpatterns = [
    path("resources", views.all_resources, name="all_resources"),
]
