from django.urls import path
from .views import TaskView, TaskDetailView, TaskFormView


urlpatterns = [
    path('tasks', TaskView, name='home'),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('addtask', TaskFormView.as_view())
]