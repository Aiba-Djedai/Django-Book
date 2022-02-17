from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "first/index.html")


def index_two(request):
    return HttpResponse('<h2>Python-Django</h2>')


def index_three(request):
    return HttpResponse('Git_Aibar')


def hello(request, name):
    return render(request, 'first/hello.html', {
        "name": name.capitalize(),
    })