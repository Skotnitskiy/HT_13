from django.shortcuts import render

from .models import Askstories


def askstories(request):
    askstories_list = Askstories.objects.all()
    return render(request, 'rep.html', {'rows': askstories_list})