from django.urls import path
from.import views

urlpatterns = [
  path('',views.todolist,name='todolist'),
  path('contactus/',views.contact,name='contactus'),
  path('aboutus/',views.about,name='aboutus')
]
