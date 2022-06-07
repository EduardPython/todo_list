from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "base/task_create.html"
    model = Task
    form_class = TaskForm

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({
            'all_tasks': Task.objects.all().filter(user=self.request.user).order_by("completed", "-created"),
        })
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "base/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    queryset = Task.objects.all()
    template_name = "base/categories.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        extra_context = {
            "family": Task.objects.filter(category=Task.CATEGORY_FAMILY).order_by("-dead_line"),
            "work": Task.objects.filter(category=Task.CATEGORY_WORK).order_by("-dead_line"),
            "garden": Task.objects.filter(category=Task.CATEGORY_GARDEN).order_by("-dead_line"),
            "household": Task.objects.filter(category=Task.CATEGORY_HOUSEHOLD).order_by("-dead_line"),
            "other": Task.objects.filter(category=Task.CATEGORY_OTHER).order_by("-dead_line"),
            'number_of_tasks': Task.objects.all().count()
        }
        context.update(extra_context)
        return context


class TaskDone(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "base/task_create.html"

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if not task.completed:
            task.completed = True
            task.save(update_fields=['completed', ])
            return redirect('tasks', )
        else:
            task.completed = False
            task.save(update_fields=['completed', ])
            return redirect('tasks', )


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")
