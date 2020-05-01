from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem



# Create your views here.
def todoView(request):
    allitems=TodoItem.objects.all()
    return render(request,'todo/todo.html',{'allit':allitems})


def addTodo(request):
    new_item=TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/') 

def deleteTodo(request,todo_id):
         a=TodoItem.objects.get(id=todo_id)
         a.delete()
         return HttpResponseRedirect('/todo/') 