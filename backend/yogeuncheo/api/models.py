from django.db import models

# Create your models here.


class TotalAddress(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    gu = models.CharField(max_length=200, blank=True, null=True)
    dong = models.CharField(max_length=200, blank=True, null=True)
    mac_score = models.FloatField(default=0.0, blank=True, null=True)
    lot_score = models.FloatField(default=0.0, blank=True, null=True)
    burgerking_score = models.FloatField(default=0.0, blank=True, null=True)
    starbucks_score = models.FloatField(default=0.0, blank=True, null=True)
    cu_score = models.FloatField(default=0.0, blank=True, null=True)
    gs25_score = models.FloatField(default=0.0, blank=True, null=True)

    seveneleven_score = models.FloatField(default=0.0, blank=True, null=True)
    megabox_score = models.FloatField(default=0.0, blank=True, null=True)
    lottecinema_score = models.FloatField(default=0.0, blank=True, null=True)

    cgv_score = models.FloatField(default=0.0, blank=True, null=True)
    total_score = models.FloatField(default=0.0, blank=True, null=True)
    total = models.IntegerField(default=0, blank=True, null=True)
    catch = models.IntegerField(default=0, blank=True, null=True)
    percent = models.FloatField(default=0.0, blank=True, null=True)

    oil1 = models.FloatField(default=0.0, blank=True, null=True)
    oil2 = models.FloatField(default=0.0, blank=True, null=True)
    oil3 = models.FloatField(default=0.0, blank=True, null=True)

    mac_count = models.IntegerField(default=0, blank=True, null=True)
    lot_count = models.IntegerField(default=0, blank=True, null=True)
    burgerking_count = models.IntegerField(default=0, blank=True, null=True)
    starbucks_count = models.IntegerField(default=0, blank=True, null=True)
    cu_count = models.IntegerField(default=0, blank=True, null=True)
    gs25_count = models.IntegerField(default=0, blank=True, null=True)
    seveneleven_count = models.IntegerField(default=0, blank=True, null=True)
    megabox_count = models.IntegerField(default=0, blank=True, null=True)
    lottecinema_count = models.IntegerField(default=0, blank=True, null=True)
    cgv_count = models.IntegerField(default=0, blank=True, null=True)
    total_count = models.IntegerField(default=0, blank=True, null=True)

    final_score= models.FloatField(default=0.0, blank=True, null=True)


#
# class SeoulLocation(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#
#
# class Apartment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)
#
#
# class FoodStore(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)
#
#
# class LocalPrice(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     location = models.ForeignKey(SeoulLocation, on_delete=models.CASCADE)