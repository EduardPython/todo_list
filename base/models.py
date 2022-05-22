from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    PRIORITY_HIGH = "high"
    PRIORITY_NORMAL = "normal"
    PRIORITY_LOW = "low"

    PRIORITY_CHOICES = (
        (PRIORITY_HIGH, "Must do"),
        (PRIORITY_NORMAL, "Should do"),
        (PRIORITY_LOW, "Nice to do")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default="normal", max_length=15)  # there must be a "max_lenght" attribute

    dead_line = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=21, default='no_category')

    def __str__(self):
        return self.description[:30]

    # class Meta:
    #     ordering = ["completed"]

