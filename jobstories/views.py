from django.shortcuts import render

from main.models import Category
from .models import Jobstories


def jobstories(request):
    categories = Category.objects.all()
    jobstories_list = Jobstories.objects.all()
    context = {
        'rows': jobstories_list,
        'categories': categories
    }
    return render(request, 'rep.html', context)
