from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
# Create your views here.
def todolist(request):
   if request.method == 'POST':
      form=TaskForm(request.POST)
      if form.is_valid():
         form.save()
      messages.success(request,'Task Added Successfully !!!')
      return redirect('todolist')
   else:
      all_task=TaskList.objects.all
      return render(request,'todolist.html',{'all_task':all_task})

def contact(request):
   context={'contact_text':'welcome to contact page'}
   return render(request,'contact.html',context)


def about(request):
   context={'about_text':'welcome to about page'}
   return render(request,'about.html',context)