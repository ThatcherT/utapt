from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.aboutme = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'

    user.save()
    context = {'user': user}
    return render(request, 'register/myfile.html', context)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)