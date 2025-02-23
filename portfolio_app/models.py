from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=250)
    image = models.ImageField(upload_to='projects/')
    repo_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    

class Technology(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    
    def __str__(self):
        return self.name
    
class WorkExperience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    
    def __str__(self):
        return self.title
