from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.TextField(null=True,blank=True)
    duration=models.IntegerField()
    fees=models.IntegerField()

    def __str__(self):
        return f"{self.name}"