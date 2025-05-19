from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    """
    Display a list of tasks.

    Parameters:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying the list of tasks.
    """
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    """
    Display details of a single task.
    Parameters:
        request (HttpRequest): The incoming HTTP request object.
        pk (int): The task identifier.
    Returns:
        HttpResponse: Rendered HTML page displaying the task details.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    """
    Create a new task.
    Parameters:
        request (HttpRequest): The incoming HTTP request object.
    Returns:
        HttpResponse: Rendered HTML page displaying the task form for creating a new task
        and after creating render task listing
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    """
    Update a task.
    Parameters:
        request (HttpRequest): The incoming HTTP request object.
        pk (int): The task identifier.
    Returns:
        HttpResponse: Rendered HTML page displaying the task form and after updating render task listing.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    """
    Delete a task.
    Parameters:
        request (HttpRequest): The incoming HTTP request object.
        pk (int): The task identifier.
    Returns:
        HttpResponse: Rendered HTML page displaying the task listing after deletion.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
