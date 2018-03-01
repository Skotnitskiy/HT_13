from django.shortcuts import render

from .models import Newstories
from main.models import Category


def newstories(request):
    newstories_list = Newstories.objects.all()
    categories = Category.objects.all()
    context = {
        'rows': newstories_list,
        'categories': categories
    }
    return render(request, 'rep.html', context)
