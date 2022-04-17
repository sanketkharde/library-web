from unicodedata import name
from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
   path('home', views.home, name='home'),
   path('load_form', views.load_form, name='load_form'),
   path('add', views.add, name='add'),
   path('show', views.show, name='show'),
   path('edit/<int:id>', views.edit, name='edit'),
   path('update/<int:id>', views.update, name='update'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('search', views.search, name='search'),
   path('register', views.register, name='register'),
   path('login', views.login, name='login'),
   path('logout', views.logout, name='logout'),
   path('first', views.first, name='first'),
   path('test', views.test, name='test'),




]

