from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'protwo'

urlpatterns = [
    path('',views.index, name='index'),
    path('user',views.user, name='user'),
    # path('forms',views.forms_view,name='forms'),
]