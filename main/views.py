from django.shortcuts import render
from rest_framework import viewsets

from main.models import Category
from main.serializers import CategoriesSerializer, AskstoriesSerializer, NewstoriesSerializer, JobstoriesSerializer, \
    ShowstoriesSerializer
from askstories.models import Askstories
from newstories.models import Newstories
from jobstories.models import Jobstories
from showstories.models import Showstories


def index(request):
    categories = Category.objects.all()
    table_rows = categories.first().askstories_set.all()
    context = {
        'rows': table_rows,
        'categories': categories
    }
    return render(request, 'rep.html', context)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class AskstoriesViewSet(viewsets.ModelViewSet):
    queryset = Askstories.objects.all()
    serializer_class = AskstoriesSerializer


class NewstoriesViewSet(viewsets.ModelViewSet):
    queryset = Newstories.objects.all()
    serializer_class = NewstoriesSerializer


class JobstoriesViewSet(viewsets.ModelViewSet):
    queryset = Jobstories.objects.all()
    serializer_class = JobstoriesSerializer


class ShowstoriesViewSet(viewsets.ModelViewSet):
    queryset = Showstories.objects.all()
    serializer_class = ShowstoriesSerializer