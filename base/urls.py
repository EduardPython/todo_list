from django.urls import path
from .views import TaskCreateView, CategoryListView, TaskDone
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", TaskCreateView.as_view(), name="tasks"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("task_done/<int:pk>", TaskDone.as_view(), name="task_done"),
    # path("/g", TaskCreateView.as_view(), name="task_create"),
]

urlpatterns += staticfiles_urlpatterns()
