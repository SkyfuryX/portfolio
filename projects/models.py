from django.db import models
from datetime import datetime
from django_resized import ResizedImageField

class Project(models.Model):
    images = models.ForeignKey('ProjectImage', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    LangChoices = {
        "PY" : "Python",
        "GO" : "Golang",
        "SQ" : "SQL",
        "OT" : "Other"
    }
    language = models.CharField(choices=LangChoices, max_length=2, default = "PY")
    tech = models.CharField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(default="", null=False)
    repo = models.CharField(max_length=100, blank = True)
    
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    title = models.ForeignKey(Project, on_delete=models.PROTECT)
    cover_image = models.ImageField(upload_to="images", null=True, blank=True)
    thumbnail = ResizedImageField(size=[425, 225], crop=['top', 'center'], upload_to="thumbnails", blank=True)
    
    def __str__(self):
        return self.title.title
