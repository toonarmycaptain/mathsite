from django.http import HttpResponse
from django.shortcuts import render

from resources.models import Resource, Subject, Topic


# Create your views here.


# view resources
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


# add resource

# edit resource
