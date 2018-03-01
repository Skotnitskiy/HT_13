from django.shortcuts import render

from main.models import Category


def index(request):
    categories = Category.objects.all()
    table_rows = categories.first().askstories_set.all()
    context = {
        'rows': table_rows,
        'categories': categories
    }
    return render(request, 'rep.html', context)
