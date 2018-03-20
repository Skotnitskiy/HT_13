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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import api_parser.views
import askstories.views
import jobstories.views
import main.views
import newstories.views
import showstories.views

router = routers.DefaultRouter()
router.register(r'api/categories', main.views.CategoriesViewSet)
router.register(r'api/askstories', main.views.AskstoriesViewSet)
router.register(r'api/jobstories', main.views.JobstoriesViewSet)
router.register(r'api/newstories', main.views.NewstoriesViewSet)
router.register(r'api/showstories', main.views.ShowstoriesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobstories/', jobstories.views.jobstories),
    path('newstories/', newstories.views.newstories),
    path('showstories/', showstories.views.showstories),
    path('askstories/', askstories.views.askstories),
    path('parse/', api_parser.views.parse),
    path('parse/<str:category>', api_parser.views.parse_category),
    path('', main.views.index),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]