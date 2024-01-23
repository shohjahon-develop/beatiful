from django.db import models

class Maxsulotlar(models.Model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=300)
    img = models.ImageField(upload_to='products/img')
    cost = models.IntegerField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    img = models.ImageField(upload_to='client/img')

    def __str__(self):
        return self.name



