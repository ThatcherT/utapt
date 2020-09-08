from django.shortcuts import render
from .models import Sublease
# Create your views here.
def search(request):
    sublease_list = Sublease.objects.all()
    context = {'sublease_list': sublease_list
               }

    return render(request, 'subl/search.html', context)