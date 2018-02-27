from django.shortcuts import render

from .models import Jobstories


def jobstories(request):
    jobstories_list = Jobstories.objects.all()
    return render(request, 'rep.html', {'rows': jobstories_list})
