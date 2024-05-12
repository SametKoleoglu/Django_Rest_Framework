from django.db import models


class Journalist(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class News(models.Model):
    journalist = models.ForeignKey(Journalist, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    city = models.CharField(max_length=100) 
    release_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title