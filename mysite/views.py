from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Projects


# Create your views here.
def index(request):
    title = "Awwards-Clone"
    projects = Projects.objects.all()
    context = {
        "title": title,
        "projects": projects,
    }
    return render(request, 'index.html', context)


def Registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"form": form})
