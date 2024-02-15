"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',views.homepage),
    path('save/',views.save),
    path('delete/',views.delete),
    path('update/',views.update),
    path('create_posts/',views.create_post),
    path('get_or_create_posts/',views.get_or_create_post),
    path('bulk_create_posts/',views.bulk_create_post),
    path('update_posts/',views.update_post),
    path('update_or_create_posts/',views.update_or_create_post),
    path('bulk_update_posts/',views.bulk_update_post),
    path('get_posts/',views.get_post),
    path('get_Q_filter_posts/',views.get_Q_filter_post),
    path('get_lookup_posts/',views.get_lookup_post),
]
