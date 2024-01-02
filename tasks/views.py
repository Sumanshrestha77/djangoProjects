from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# tasks = []

class NewTaskForm(forms.Form):
    task= forms.CharField(label="New Task")
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] =[]
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    #server side validation
    if request.method == "POST":
        form = NewTaskForm(request.POST) #this gets the submitted value of form
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form":form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })