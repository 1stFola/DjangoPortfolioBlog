from cgitb import html
from pydoc import describe
from tkinter.tix import Form
from turtle import title
from django.shortcuts import redirect, render
from  django.contrib import messages

import projects
from .forms import ProjectForm
from .models import Project


def create_project(request):
    data = request.POST
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(data=data)
        title = data.get('title')
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            form = ProjectForm()
            messages.success(request, f"{title} just got created")
            return redirect('view_all_projects')
        else:
            messages.error(request, "Person ")
    return render(request, "projects/create_project.html", {"form": form})


def get_projects(request):
    data = request.POST
    if data:
        key = data.get('filter')
        projects = {} if key is None else Project.objects.filter(title__contains=key)
    else:
        projects = Project.objects.all().order_by('-date_created')
    return render(request, "projects/project_list.html", {"projects": projects})


def filter_projects(request):
    data = request.POST
    key = data.get('filter')
    if key is not None:
        projects = Project.objects.filter(title__contains=key)
    else:
        projects = {}
    return render(request, "projects/filtered_projects.html", {'projects': projects})

def retrieve_projects(request, id):
    if Project.objects.filter(id=id).exists():
        project = Project.objects.get(id=id)
    else:
        project = {}
    return render(request, 'projects/project_detail.html', {'project': project})

def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    data = request.POST
    print(data)
    if request.method == "POST":
        form = ProjectForm(instance=project, data=data)
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            print("here")
            return redirect('retrieve_projects', id)
        else:
            print("This can not be saved")
            print("The technology should not be paerson")
            print(form.errors)   #a function to save submitted forms
            
    return render(request, "projects/update_project.html", {'project': project, 'form': form})


def delete_project(request, id):
    if Project.objects.filter(id=id).exists():
        Project.objects.get(id=id).delete()        
        print('Project successfully deleted')
    return redirect('view_all_projects')
