from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    form = TForm()

    if request.method=="POST":
        form = TForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    content = {"tasks":tasks, "form":form}

    return render(request, "tasks/index.html", content)

def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TForm(instance=task)

    if request.method == "POST":
        form = TForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    content = {"form":form}
    return render(request, "tasks/updatetask.html", content)

def delete(request, pk):
    task = Tasks.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")
    content = {"task":task}
    return render(request, "tasks/delete.html", content)