from django.urls import path
from . import views

urlpatterns = [
    path("toDo/", views.ToDoView.as_view())
]