from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Task

from django.contrib.auth.views import LoginView


class TaskLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class TaskCreateView(CreateView):
    template_name = "base/task_create.html"
    model = Task
    fields = ["category", "name", "description", "priority", "to_do", "dead_line"]
    success_url = reverse_lazy("tasks")

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({
            'all_tasks': Task.objects.all().order_by("completed", "dead_line", "priority", "-created"),
        })
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "base/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context


class CategoryListView(ListView):
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


class TaskDone(DetailView):
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


class DeleteTaskView(DeleteView):
    model = Task
    #  template_name = "base/task_confirm_delete.html"
    success_url = reverse_lazy("tasks")
