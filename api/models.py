from django.db import models


class Company(models.Model):
    name=models.CharField(max_length=50)
    dir=models.CharField(max_length=50)
    nit=models.CharField(max_length=15)
    tel=models.CharField(max_length=15)

