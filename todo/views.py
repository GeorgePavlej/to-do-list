from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TaskCreationForm, TaskUpdateForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TagListview(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    models = Tag
    fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


def task_status(request, pk):

    task = Task.objects.get(pk=pk)
    task.progress = not task.progress
    task.save()

    return redirect(reverse("todo:task-list"))
