from django.db import models
from django.shortcuts import reverse

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.TextField(null=True,blank=True)
    duration=models.IntegerField()
    fees=models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('list-course')