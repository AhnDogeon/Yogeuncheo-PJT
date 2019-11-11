from django.db import models

# Create your models here.

class TotalAddress(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    gu = models.CharField(max_length=100, blank=True, null=True)
    dong = models.CharField(max_length=100, blank=True, null=True)
    mac_score = models.FloatField(default=0.0, blank=True, null=True)
    lot_score = models.FloatField(default=0.0, blank=True, null=True)
    burgerking_score = models.FloatField(default=0.0, blank=True, null=True)
    seveneleven_score = models.FloatField(default=0.0, blank=True, null=True)
    cu_score = models.FloatField(default=0.0, blank=True, null=True)
    gs25_score = models.FloatField(default=0.0, blank=True, null=True)
    starbucks_score = models.FloatField(default=0.0, blank=True, null=True)
    lottecinema_score = models.FloatField(default=0.0, blank=True, null=True)
    megabox_score = models.FloatField(default=0.0, blank=True, null=True)
    cgv_score = models.FloatField(default=0.0, blank=True, null=True)
    total_score = models.FloatField(default=0.0, blank=True, null=True)

    high_oil = models.FloatField(default=0.0, blank=True, null=True)
    oil = models.FloatField(default=0.0, blank=True, null=True)
    oil2 = models.FloatField(default=0.0, blank=True, null=True)

    total = models.IntegerField(default=0,blank=True,null=True)
    catch = models.IntegerField(default=0,blank=True,null=True)
    percent = models.FloatField(default=0.0,blank=True,null=True)

    mac_count = models.IntegerField(default=0, blank=True, null=True)
    lot_count = models.IntegerField(default=0, blank=True, null=True)
    burgerking_count = models.IntegerField(default=0, blank=True, null=True)
    seveneleven_count = models.IntegerField(default=0, blank=True, null=True)
    cu_count = models.IntegerField(default=0, blank=True, null=True)
    gs25_count = models.IntegerField(default=0, blank=True, null=True)
    starbucks_count = models.IntegerField(default=0, blank=True, null=True)
    lottecinema_count = models.IntegerField(default=0, blank=True, null=True)
    megabox_count = models.IntegerField(default=0, blank=True, null=True)
    cgv_count = models.IntegerField(default=0, blank=True, null=True)
    total_count = models.IntegerField(default=0, blank=True, null=True)

    first = models.CharField(max_length=100, blank=True, null=True)
    second = models.CharField(max_length=100, blank=True, null=True)
    third = models.CharField(max_length=100, blank=True, null=True)

    first_mapx = models.FloatField(default=0.0, blank=True, null=True)
    first_mapy = models.FloatField(default=0.0, blank=True, null=True)
    second_mapx = models.FloatField(default=0.0, blank=True, null=True)
    second_mapy = models.FloatField(default=0.0, blank=True, null=True)
    third_mapx = models.FloatField(default=0.0, blank=True, null=True)
    third_mapy = models.FloatField(default=0.0, blank=True, null=True)

    elementary_count = models.IntegerField(default=0, blank=True, null=True)
    middle_count = models.IntegerField(default=0, blank=True, null=True)
    high_count = models.IntegerField(default=0, blank=True, null=True)
    park_count = models.IntegerField(default=0, blank=True, null=True)
    station = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.address)