from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import TaskCreateView, CategoryListView, TaskDone, DeleteTaskView, TaskDetailView, TaskLoginView, \
    ListByCategories, TaskEditView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("login/", TaskLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="tasks"), name="logout"),
    path("register/", views.register_request, name="register"),

    path("", TaskCreateView.as_view(), name="tasks"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("task_done/<int:pk>", TaskDone.as_view(), name="task_done"),
    # path("task_edit/<int:pk>", TaskEditView.as_view(), name="task_edit"),
    path("task_detail/<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("task_delete/<int:pk>/", DeleteTaskView.as_view(), name="delete_task"),
    # path("/g", TaskCreateView.as_view(), name="task_create"),
    path("list_by_categories/<str:category>/", ListByCategories.as_view(), name="list_by_categories"),
    path("categories/<str:category>/", ListByCategories.as_view(), name="list_by_categories"),
    path("task_edit/<int:pk>", TaskEditView.as_view(), name="task_edit"),
]

urlpatterns += staticfiles_urlpatterns()
