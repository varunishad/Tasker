from django.urls import path, include
from . import views

urlpatterns = [
    # path("create/", views.create_task, name="create_task"),
    path("api/tasks/",views.TaskListCreate.as_view(), name="task-list-create"),
    path("api/tasks/<int:pk>/",views.TaskRetrieveUpdateDestroy.as_view() ,name="task-details")
]
