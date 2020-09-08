from django.shortcuts import render
from .models import RoommateProfile
# Create your views here.
def search(request):
    roommate_list = RoommateProfile.objects.all()
    context = {'roommate_list': roommate_list
               }

    return render(request, 'roomm/search.html', context)