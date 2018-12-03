"""try_django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='create'),
    path('<int:id>/', views.posts_detail, name='detail'),
    path('<int:id>/edit/', views.posts_update, name='update'),
    path('<int:id>/delete/', views.posts_delete, name='delete'),
]
