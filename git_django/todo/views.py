from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class Todo(forms.Form):
    task = forms.CharField(label="New todo")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todo/index.html", {
        "todo": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = Todo(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/add.html", {
                "form": form
            })

    return render(request, "todo/add.html", {
        "form": Todo()
    })