"""project44 URL Configuration

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
from django.urls import path,re_path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home.as_view(),name='home'),
    path('list_school/',list_school.as_view(),name='list_school'),
    path('schoolcreate/',schoolcreate.as_view(),name='schoolcreate'),


    re_path('^update/(?P<pk>\d+)/',schoolupdate.as_view(),name='schoolupdate'),

    re_path('^delete(?P<pk>\w+)/',schooldelete.as_view(),name='schooldelete'),

    re_path('(?P<pk>\d+)/',schooldetail.as_view(),name='schooldetail'),
]
