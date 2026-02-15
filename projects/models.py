from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Project(models.Model):
    cover_image = models.ImageField(upload_to="images", null=True)
    title = models.CharField(max_length=100)
    tech = models.CharField()
    description = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(default=slugify(title))
    
    def __str__(self):
        return self.title