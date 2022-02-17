from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:name>', views.hello, name='hello'),
    path('two', views.index_two, name='index_two'),
    path('three', views.index_three, name='index_three'),
]