from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Task


# class TaskListView(ListView):
#     model = Task
#     template_name = "base/base.html"


class TaskCreateView(CreateView):
    template_name = "base/task_create.html"
    model = Task
    fields = ["description", "priority"]
    success_url = reverse_lazy("tasks")

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({
            'all_tasks': Task.objects.all().order_by("-created"),
        })
        return context

