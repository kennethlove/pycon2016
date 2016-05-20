from django.contrib.auth.models import User
from django.db import models

DIFFICULTY_LEVELS = (
    (1, 'beginner'),
    (2, 'intermediate'),
    (3, 'advanced'),
)

INTENSITY_LEVELS = (
    (1, 'low'),
    (2, 'moderate'),
    (3, 'high'),
)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="duration in minutes")
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS, default=1)
    intensity = models.IntegerField(choices=INTENSITY_LEVELS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserExercise(models.Model):
    user = models.ForeignKey(User, related_name="exercises")
    exercise = models.ForeignKey(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)
