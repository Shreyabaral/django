from django.db import models
from django.utils import dates, timezone


# Create your models here.
class Authors(models.Model):
    Name = models.CharField(max_length=100)
    Genre= models.CharField(max_length=100)
    Bio = models.TextField()
    def __str__(self):
        return self.Name

class blogPost(models.Model):
    Title= models.CharField(max_length=100)
    Text = models. TextField()
    Created_date = models.DateTimeField(default=timezone.now)
    Updated_date = models.DateTimeField(blank=True, null=True)
    Author = models.ForeignKey(Authors, related_name='blogPost', on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
