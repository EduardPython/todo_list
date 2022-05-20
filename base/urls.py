from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    path("", TaskCreateView.as_view(), name="tasks"),
    #path("/g", TaskCreateView.as_view(), name="task_create"),
]
