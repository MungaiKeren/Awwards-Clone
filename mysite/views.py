from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import *
from .models import Projects
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    title = "Awwards-Clone"
    projects = Projects.get_projects()
    current_user = request.user
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


@login_required(login_url='/login/')
def Registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"form": form})


@login_required(login_url='/login')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('/')
    else:
        form = PostProjectForm(auto_id=False)
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/login/')
def get_project(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
        print(project)
    except DoesNotExist:
        raise Http404()
    return render(request, 'project.html', {"project": project})


def search_results(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get('projects')
        searched_projects = Projects.search_by_title(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "projects": searched_projects
        }
        return render(request, 'search.html', context)
    else:
        message = "Search a project by title"
        return render(request, 'search.html', {"message": message})
