"""srw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from dbapp import views

urlpatterns = [
    # path('', views.home),
    path('index', views.index),
<<<<<<< Updated upstream
    path('create', views.create),
    # path('admin/', admin.site.urls),
    # path('', views.index),
=======
    # path('create', views.create),
    path('search', views.search),
    path('test', views.test),
    path('test_search', views.test_search),
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
>>>>>>> Stashed changes
]
