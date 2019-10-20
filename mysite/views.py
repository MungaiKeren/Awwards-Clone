from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import *
from .models import Projects
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    title = "Awwards-Clone"
    projects = Projects.get_projects()
    context = {
        "title": title,
        "projects": projects,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def Profile(request):
    pics = Projects.get_projects()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
    return render(request, 'profile.html', {"u_form": u_form, "p_form": p_form, "pics": pics})


def Registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"form": form})


def single_page(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'project.html', {"project": project})
