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
    fields = ["category", "description", "priority", "dead_line"]
    success_url = reverse_lazy("tasks")

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({
            'all_tasks': Task.objects.all().order_by("-created"),
        })
        return context


class CategoryListView(ListView):
    queryset = Task.objects.all()
    template_name = "categories.html"
    extra_context = {
        "family": Task.objects.filter(category=Task.CATEGORY_FAMILY).order_by("-dead_line"),
        "work": Task.objects.filter(category=Task.CATEGORY_WORK).order_by("-dead_line"),
        "garden": Task.objects.filter(category=Task.CATEGORY_GARDEN).order_by("-dead_line"),
        "household": Task.objects.filter(category=Task.CATEGORY_HOUSEHOLD).order_by("-dead_line"),
        "other": Task.objects.filter(category=Task.CATEGORY_OTHER).order_by("-dead_line")
    }
