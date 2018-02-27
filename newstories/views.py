from django.shortcuts import render

from .models import Newstories


def newstories(request):
    newstories_list = Newstories.objects.all()
    return render(request, 'rep.html', {'rows': newstories_list})
