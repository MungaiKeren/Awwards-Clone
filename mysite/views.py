from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"form": form})
