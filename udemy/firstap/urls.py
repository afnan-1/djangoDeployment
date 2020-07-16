from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('forms',views.forms_view,name='forms'),
    path('register',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
]