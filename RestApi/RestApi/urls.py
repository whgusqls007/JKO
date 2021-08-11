"""RestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("read_busan/", views.read_busan),
    path("read_ohmynews/", views.read_ohmynews),
    path("read_wikitree/", views.read_wikitree),
    path("read_herald/", views.read_herald),
    path("read_nocut/", views.read_nocut),
    path("read_yeonhap/", views.read_yeonhap),
    path("read_donga/", views.read_donga),
    path("read_joongang/", views.read_joongang),
    path("read_joseon/", views.read_joseon),
    path("read_hangook/", views.read_hangook),
]
