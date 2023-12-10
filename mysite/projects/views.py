from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project

# Create your views here.

def home(request):
    projects_list = Project.objects.all()
    paginator = Paginator(projects_list, 3)

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, "projects/home.html", {"projects": projects})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)

    # Pass the current page to the template context
    current_page = request.GET.get('page')
    return render(request, "projects/detail.html", {"project": project_detail, "current_page": current_page})

