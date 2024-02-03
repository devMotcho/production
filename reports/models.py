from django.db import models
from django.urls import reverse

#my apps imports
from human.models import Profile



class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='reports', blank=True)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.created})'

    class Meta:
        ordering = ['-created']
