from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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
    
class ViewProj(DetailView):
    model = Project

class EditProj(UpdateView):
    model = Project

class AddProj(CreateView):
    model = Project
