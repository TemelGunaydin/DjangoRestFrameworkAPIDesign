from django.urls import path
from . import views

urlpatterns = [ path('todos',views.todos,name='todos'),
        path('todos/<str:pk>',views.todo_list,name='todo_list')]

