from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task


def index_view(request: WSGIRequest):
    task_list = Task.objects.all()
    if task_list:
        context = {'task_list': task_list}
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'index.html')


def create_task(request: WSGIRequest):
    if request.method == 'GET':
        context = {'statuses': Task.STATUSES}
        return render(request, 'add_task.html', context=context)
    elif request.method == 'POST':
        task_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'deadline': request.POST.get('deadline')
        }
        task = Task.objects.create(**task_data)
        task.save()
        return redirect('detail', pk=task.pk)


def task_detail(request: WSGIRequest, pk):
    context = {'task': get_object_or_404(Task, pk=pk)}
    return render(request, 'task_detail.html', context=context)


def update_task(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        context = {
            'task': task,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'deadline': task.deadline,
            'statuses': Task.STATUSES
        }
        return render(request, 'update_task.html', context=context)
    elif request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('detail', pk=task.pk)


def delete_task(request, pk):
    print(pk, 'pk')
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
