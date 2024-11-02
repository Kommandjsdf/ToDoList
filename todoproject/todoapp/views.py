
from django.http import HttpResponseRedirect
from django.shortcuts import render

from todoapp.models import TodoListItem


# Create your views here.

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, "index.html", {"all_items":all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoAppView/')

def deleteTodoView(request):
    return HttpResponseRedirect('/deleteTodoAppView/')

def deleteTodoAppView(request):
    all_todo_items = TodoListItem.objects.all()
