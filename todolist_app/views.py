from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def todolist(request):
   if request.method == 'POST':
      form=TaskForm(request.POST)
      if form.is_valid():
         form.save()
      messages.success(request,'Task Added Successfully !!!')
      return redirect('todolist')
   else:
      all_task=TaskList.objects.all()
      paginator = Paginator(all_task,10)
      page = request.GET.get('pg')
      all_task = paginator.get_page(page)
      return render(request,'todolist.html',{'all_task':all_task})

def delete_task(requst,task_id):
   task=TaskList.objects.get(pk=task_id)
   task.delete()
   return redirect('todolist')

def edit_task(request,task_id):
   if request.method == 'POST':
      task=TaskList.objects.get(pk=task_id)
      form=TaskForm(request.POST or None, instance = task)
      if form.is_valid():
         form.save()
      messages.success(request,'Task Edited Successfully !!!')
      return redirect('todolist')
   else:
      task_obj=TaskList.objects.get(pk=task_id)
      return render(request,'edit.html',{'task_obj':task_obj})
   

def complete_task(requst,task_id):
   task=TaskList.objects.get(pk=task_id)
   task.done= True
   task.save()
   return redirect('todolist')

def pending_task(requst,task_id):
   task=TaskList.objects.get(pk=task_id)
   task.done= False
   task.save()
   return redirect('todolist')
   
def contact(request):
   context={'contact_text':'welcome to contact page'}
   return render(request,'contact.html',context)


def about(request):
   context={'about_text':'welcome to about page'}
   return render(request,'about.html',context)