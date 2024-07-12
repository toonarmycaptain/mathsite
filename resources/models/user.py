# User model
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=24)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    # profile_picture = models.ImageField(upload_to="profile_pictures")  # TODO: implement. Omit for now as requires Pillow

    # password = models.CharField(max_length=128)  # Implement here or in auth/elsewhere?

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
