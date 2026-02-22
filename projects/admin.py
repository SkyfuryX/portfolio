from django.contrib import admin
from .models import Project, ProjectImage


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]} 
    
@admin.register(ProjectImage) 
class ProjImageAdmin(admin.ModelAdmin):
    pass