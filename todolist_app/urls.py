from django.urls import path
from.import views

urlpatterns = [
  path('',views.todolist,name='todolist'),
  path('delete/<task_id>',views.delete_task,name='delete_task'),
  path('edit_task/<task_id>',views.edit_task,name='edit_task'),
  path('complete_task/<task_id>',views.complete_task,name='complete_task'),
  path('pending_task/<task_id>',views.pending_task,name='pending_task'),
  path('contactus/',views.contact,name='contactus'),
  path('aboutus/',views.about,name='aboutus')
]
