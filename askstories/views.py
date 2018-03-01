from django.shortcuts import render

from askstories.models import Askstories
from main.models import Category


def askstories(request):
    categories = Category.objects.all()
    askstories_list = Askstories.objects.all()
    context = {
        'rows': askstories_list,
        'categories': categories
    }
    return render(request, 'rep.html', context)
