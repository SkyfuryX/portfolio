from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from datetime import date

class HomePage(ListView):
    model = Project
    template_name = "home.html"
    context_object_name = "projects"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context
    
class ProjectDetail(DetailView):
    model = Project
    slug_field = "slug"
    template_name = "detail.html"    

class ProjectEdit(LoginRequiredMixin, UpdateView):
    model = Project
    slug_field = "slug"
    login_url = 'home'

class ProjectNew(LoginRequiredMixin, CreateView):
    model = Project
    login_url = 'home'
