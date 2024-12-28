from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CoustomCreationForm

def register(request):
    if request.method == 'POST':
        register_form=CoustomCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'New Account is Created, Login to Gets Started!')
            return redirect('register')
    else:
        register_form=CoustomCreationForm()
    return render(request,'register.html',{'register_form':register_form})

def logout_user(request):
    logout(request)
    return render(request,'logout.html')
