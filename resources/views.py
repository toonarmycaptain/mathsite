from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from resources.models import Resource, Subject, Topic


# Create your views here.


# view resources
# @login_required()
def all_resources(request) -> HttpResponse:
    # gather resources, nested by subject and topic
    resources = {}
    for subject in Subject.objects.all():
        resources[subject.short_name] = {}
        for topic in Topic.objects.all():
            if topic_resources := Resource.objects.filter(
                subject=subject, topic=topic
            ).all():
                resources[subject.short_name][topic.short_name] = topic_resources

    return render(request, "resources/all_resources.html", {"resources": resources})


def edit_resource(request, id):
    resource = get_object_or_404(Resource, id=id)
    return render(
        request,
        template_name="resources/edit_resource.html",
        context=dict(resource=resource),
    )


def view_resource(request, id):
    resource = get_object_or_404(Resource, id=id)
    return render(
        request,
        template_name="resources/single_resource.html",
        context=dict(resource=resource),
    )


# edit resource
def update_resource(request, id):
    resource = get_object_or_404(Resource, id=id)
    resource.name = request.POST["name"]
    resource.save()
    return render(
        request,
        template_name="resources/single_resource.html",
        context=dict(resource=resource),
    )


def delete_resource(request, id) -> HttpResponse:
    resource = get_object_or_404(Resource, id=id)
    resource.delete()
    return render(
        request,
        template_name="resources/deleted_resource.html",
        context=dict(resource=resource),
    )


# add resource
def save_new_resource(request) -> HttpResponse:
    name = request.POST["name"]
    Resource.objects.create(name=name)
    return render(
        request,
        template_name="resources/resources_list.html",
        context=dict(resources=Resource.objects.order_by("name")),
    )
