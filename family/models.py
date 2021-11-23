from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)


# 1 to 1 relationship

class Cage(models.Model):
    name = models.CharField(max_length=100)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)