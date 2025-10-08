from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link_github = models.URLField(blank=True, null=True)
    link_demo = models.URLField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
