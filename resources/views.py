from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from resources.forms import ResourceForm
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


def view_resource(request, id):
    resource = get_object_or_404(Resource, id=id)
    return render(
        request,
        template_name="resources/single_resource.html",
        context=dict(resource=resource),
    )


# @login_required
def create_resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()

            if request.htmx:
                # Return the updated list of resources after the new resource is added
                return render(
                    request,
                    "resources/resources_list.html",
                    {"resources": Resource.objects.all()},
                )

            return redirect("resources_list")  # Fallback for non-HTMX requests
    else:
        form = ResourceForm()

    return render(request, "resources/create_resource.html", {"form": form})


def update_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.updated_by = request.user  # Set the updated user
            resource.save()

            if request.htmx:
                # Return the updated resource row or a success message
                return render(
                    request, "resources/resource_row.html", {"resource": resource}
                )

            return redirect("resources_list")
    else:
        form = ResourceForm(instance=resource)

    if request.htmx:
        # If HTMX request, return the form for editing
        return render(
            request,
            "resources/update_resource.html",
            {"form": form, "resource": resource},
        )

    # Fallback if not HTMX (regular HTTP request)
    return render(
        request, "resources/update_resource.html", {"form": form, "resource": resource}
    )


def delete_resource(request, id) -> HttpResponse:
    resource = get_object_or_404(Resource, id=id)
    resource.delete()
    return render(
        request,
        template_name="resources/deleted_resource.html",
        context=dict(resource=resource),
    )
