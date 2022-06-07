from datetime import timedelta
from django import forms
from django.utils import timezone

from .models import Task


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(CustomDateInput, self).__init__(*args, **kwargs)


def tomorrow():
    return timezone.now() + timedelta(days=1)


def one_week_later():
    return timezone.now() + timedelta(days=7)


class TaskForm(forms.ModelForm):

    to_do = forms.DateField(widget=CustomDateInput(), initial=tomorrow)
    dead_line = forms.DateField(widget=CustomDateInput(), initial=one_week_later)

    class Meta:
        model = Task
        exclude = ["user", "created", "completed", ]       # there must be either "exclude" or "fields"