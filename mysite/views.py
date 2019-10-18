from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm


# Create your views here.
def index(request):
    title = "Awwards-Clone"
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)


def Registration(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html', {"form":form})
