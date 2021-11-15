from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length= 300)
    email=models.CharField(max_length=400)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name
