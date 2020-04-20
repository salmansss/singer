from django.db import models

# Create your models here.

class femalesinger(models.Model):
    alphabatletterofsingers = models.CharField(max_length=50)
    namesofsingers = models.CharField(max_length=50)
    linkofsinger = models.CharField(max_length=150)

    def __str__(self):
        return self.alphabatletterofsingers


class malesinger(models.Model):
    alphabatletterofsingers = models.CharField(max_length=50)
    namesofsingers = models.CharField(max_length=50)
    linkofsinger = models.CharField(max_length=150)

    def __str__(self):
        return self.alphabatletterofsingers