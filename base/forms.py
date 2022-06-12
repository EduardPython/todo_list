from datetime import timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from . import models
from .models import Task


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(CustomDateInput, self).__init__(*args, **kwargs)


class CustomTimeInput(forms.DateTimeInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'time'}})
        super(CustomTimeInput, self).__init__(*args, **kwargs)


def tomorrow():
    return timezone.now() + timedelta(days=1)


def one_week_later():
    return timezone.now() + timedelta(days=7)


class TaskForm(forms.ModelForm):
    to_do = forms.DateField(widget=CustomDateInput(), initial=tomorrow)
    to_do_time = forms.TimeField(widget=CustomTimeInput())
    dead_line = forms.DateField(widget=CustomDateInput(), initial=one_week_later)
    dead_line_time = forms.TimeField(widget=CustomTimeInput())

    class Meta:
        model = Task
        exclude = ["user", "created", "completed", ]  # there must be either "exclude" or "fields"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
