from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    title = "Awwards-Clone"
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)
