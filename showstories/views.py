from django.shortcuts import render

from main.models import Category
from .models import Showstories


def showstories(request):
    categories = Category.objects.all()
    showstories_list = Showstories.objects.all()
    context = {
        'rows': showstories_list,
        'categories': categories
    }
    return render(request, 'rep.html', context)
