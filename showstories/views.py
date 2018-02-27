from django.shortcuts import render


from .models import Showstories


def showstories(request):
    showstories_list = Showstories.objects.all()
    return render(request, 'rep.html', {'rows': showstories_list})
