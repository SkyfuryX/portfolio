from django.db import models
from django.core.files.base import ContentFile
from PIL import Image,ImageOps
import io

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
    thumbnail = models.ImageField(upload_to="thumbnails", null=True, blank=True)
    
    def __str__(self):
        return self.title.title

    def save(self, *args, **kwargs):
        # handle the resize safely for S3
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            img = ImageOps.fit(img, (425, 225), method=Image.Resampling.LANCZOS)
    
            #temporarily save in buffer
            buffer = io.BytesIO()
            img_format = img.format if img.format else 'JPEG'
            img.save(buffer, format=img_format, quality=85)
            
            filename = self.thumbnail.name
            self.thumbnail.save(filename, ContentFile(buffer.getvalue()), save=False)
            
        super().save(*args, **kwargs)
