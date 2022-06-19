import requests
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .models import Task
from .forms import TaskForm, NewUserForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


def get_btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data["bpi"]["USD"]["rate"][:6]


class BaseView(LoginRequiredMixin, TemplateView):       # this maybe can be deleted. It was mentioned for btc_price, but has no effect
    template_name = "base/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context.update({
            "btc_price": get_btc_price(),
        })
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "base/task_create.html"
    model = Task
    form_class = TaskForm

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({
            "all_tasks": Task.objects.all().filter(user=self.request.user).order_by("completed", "-created"),
            "btc_price": get_btc_price()
        })
        return context

    def form_valid(self, form):  # this join created task to actual user
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "base/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context.update({
            "btc_price": get_btc_price(),
        })
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "base/categories.html"

    def get_queryset(self):
        return Task.objects.all().filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        extra_context = {
            "family": Task.objects.filter(category=Task.CATEGORY_FAMILY, user=self.request.user),
            "work": Task.objects.filter(category=Task.CATEGORY_WORK, user=self.request.user),
            "garden": Task.objects.filter(category=Task.CATEGORY_GARDEN, user=self.request.user),
            "household": Task.objects.filter(category=Task.CATEGORY_HOUSEHOLD, user=self.request.user),
            "other": Task.objects.filter(category=Task.CATEGORY_OTHER, user=self.request.user),
            'number_of_tasks': Task.objects.all().filter(user=self.request.user).count(),
            "btc_price": get_btc_price(),
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
    extra_context = {
            "btc_price": get_btc_price(),
        }


class ListByCategories(LoginRequiredMixin, ListView):
    template_name = "base/list_by_categories.html"

    def get_queryset(self):
        category = self.kwargs['category']
        return Task.objects.filter(category=category, user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ListByCategories, self).get_context_data(*args, **kwargs)
        extra_context = {
            "name_of_category": self.kwargs["category"],
            "btc_price": get_btc_price(),
        }
        context.update(extra_context)
        return context


class TaskEditView(UpdateView):
    template_name = "base/task_edit.html"
    form_class = TaskForm
    model = Task
    extra_context = {
        "btc_price": get_btc_price(),
    }


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("tasks")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="base/register.html", context={"register_form": form})
