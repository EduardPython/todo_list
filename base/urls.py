from django.urls import path
from .views import TaskCreateView, CategoryListView

urlpatterns = [
    path("", TaskCreateView.as_view(), name="tasks"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    # path("/g", TaskCreateView.as_view(), name="task_create"),
]
