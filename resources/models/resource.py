# General resource classes
# NB plural name resources used to not overwrite python stl lib module 'resource'.
from django.conf import settings
from django.db import models
from django.db.models import SET_NULL, PROTECT

grade_levels = [
    (
        "elementary",
        (
            ("PK", "pre-K"),
            ("KG", "Kindergarten"),
            ("1", "First"),
            ("2", "Second"),
            ("3", "Third"),
            ("4", "Forth"),
            ("5", "Fifth"),
        ),
    ),
    (
        "middle",
        (
            ("6", "Sixth"),
            ("7", "Seventh"),
            ("8", "Eighth"),
        ),
    ),
    (
        "high",
        (
            ("9", "Ninth"),
            ("10", "tenth"),
        ),
    ),
]


# TODO: implement way of adding choices  Subjects/Topics
class Subject(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="subject_created_by", on_delete=PROTECT
    )  # This should prevent deletion of a user who has authored stuff.
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="subject_updated_by", on_delete=PROTECT
    )

    def __str__(self):
        return self.short_name


class Topic(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    subject = models.ForeignKey(Subject, on_delete=PROTECT)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="topic_created_by", on_delete=PROTECT
    )
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="topic_updated_by", on_delete=PROTECT
    )

    def __str__(self):
        return self.short_name


class Resource(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    # on_delete=SET_NULL, null=True means that if the Subject is deleted, subject will be set to null
    subject = models.ForeignKey(Subject, on_delete=SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=SET_NULL, null=True)
    grade_level = models.CharField(blank=True, max_length=2, choices=grade_levels)
    grade_level_min = models.CharField(blank=True, max_length=2, choices=grade_levels)
    grade_level_max = models.CharField(blank=True, max_length=2, choices=grade_levels)
    link = models.URLField()

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="resource_created_by", on_delete=PROTECT
    )
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="resource_updated_by", on_delete=PROTECT
    )

    def __str__(self):
        vars = [
            f"{self.short_name=}",
            f"{self.long_name=}",
            f"{self.subject=}",
            f"{self.topic=}",
            f"{self.grade_level=}",
            f"{self.grade_level_min=}",
            f"{self.grade_level_max=}",
            f"{self.active=}",
            f"{self.created=}",
            f"{self.created_by=}",
            f"{self.updated=}",
            f"{self.updated_by=}",
        ]
        return f"{self.short_name}: {vars}"
