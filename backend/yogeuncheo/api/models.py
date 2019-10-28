from django.db import models

# Create your models here.


class SeoulLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class Apartment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)


class FoodStore(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)


class LocalPrice(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)