from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            "short_name",
            "long_name",
            "description",
            "subject",
            "topic",
            "grade_level",
            "grade_level_min",
            "grade_level_max",
            "link",
            "active",
        ]
