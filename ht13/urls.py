"""ht13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import askstories.views
import jobstories.views
import main.views
import newstories.views
import showstories.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobstories/', jobstories.views.jobstories),
    path('newstories/', newstories.views.newstories),
    path('showstories/', showstories.views.showstories),
    path('askstories/', askstories.views.askstories),
    path('', main.views.index)
]
