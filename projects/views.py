from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from .models import Project
from datetime import datetime

class HomePage(TemplateView):
    template = "home.html"
    model = Project
    today = datetime.now()
    
class ViewProj(DetailView):
    model = Project

class EditProj(UpdateView):
    model = Project

class AddProj(CreateView):
    model = Project
