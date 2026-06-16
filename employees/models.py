from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    experience_years = models.FloatField()

    def __str__(self):
        return self.name