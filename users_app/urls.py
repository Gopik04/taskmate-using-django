from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.logout_user, name='logout'),
]