from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    height = models.DecimalField(
        decimal_places=2,
        help_text="in cm",
        max_digits=5
    )
    weight = models.DecimalField(
        decimal_places=2,
        help_text="in kg",
        max_digits=5
    )
