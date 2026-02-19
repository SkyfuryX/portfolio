from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Project(models.Model):
    cover_image = models.ImageField(upload_to="images", null=True, blank=True)
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
    
