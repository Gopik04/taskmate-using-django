from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
# Create your views here.
def todolist(request):
   all_task=TaskList.objects.all
   return render(request,'todolist.html',{'all_task':all_task})

def contact(request):
   context={'contact_text':'welcome to contact page'}
   return render(request,'contact.html',context)


def about(request):
   context={'about_text':'welcome to about page'}
   return render(request,'about.html',context)