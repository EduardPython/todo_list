from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    PRIORITY_HIGH = "Must do"
    PRIORITY_NORMAL = "Should do"
    PRIORITY_LOW = "Nice to do"

    PRIORITY_CHOICES = (
        (PRIORITY_HIGH, "Must do"),
        (PRIORITY_NORMAL, "Should do"),
        (PRIORITY_LOW, "Nice to do")
    )

    CATEGORY_FAMILY = "family"
    CATEGORY_WORK = "work"
    CATEGORY_GARDEN = "garden"
    CATEGORY_HOUSEHOLD = "household"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = (
        (CATEGORY_FAMILY, "Family"),
        (CATEGORY_WORK, "Work"),
        (CATEGORY_GARDEN, "Garden"),
        (CATEGORY_HOUSEHOLD, "Household"),
        (CATEGORY_OTHER, "Other")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default="normal", max_length=15)  # there must be a "max_lenght" attribute

    dead_line = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, default="other", max_length=21)

    def __str__(self):
        return self.name[:30]

    # class Meta:
    #     ordering = ["completed"]

