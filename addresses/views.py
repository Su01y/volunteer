from audioop import add
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from addresses.forms import TaskForm
from .models import Task
from django.views import generic
from django.views import View


class TaskDetailView(generic.DetailView):
    model = Task

def TaskView(request, *args, **kwargs):
    addresses = Task.objects.all().values()
    return render(request, 'addresses/home.html', {
        'addresses': addresses,
    })

class TaskFormView(View):
    
    def get(self, request):
        task_form = TaskForm()
        return render(request, 'addresses/add_task.html', context={'task_form': task_form})

    def post(self, request):
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            Task.objects.create(**task_form.cleaned_data)
            return HttpResponseRedirect('/tasks')

        return render(request, 'addresses/add_task.html', context={'task_form': task_form})
