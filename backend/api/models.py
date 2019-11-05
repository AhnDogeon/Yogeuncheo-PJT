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

    def __str__(self):
        return "{}: {}".format(self.id, self.address)


def create_data(**kwargs):
    totaladd = TotalAddress.objects.create(
        address=kwargs['address'],
        gu=kwargs['gu'],
        dong=kwargs['dong'],
        mac_score=kwargs['mac_score'],
        lot_score=kwargs['lot_score'],
        burgerking_score=kwargs['burgerking_score'],
        seveneleven_score=kwargs['seveneleven_score'],
        cu_score=kwargs['cu_score'],
        gs25_score=kwargs['gs25_score'],
        starbucks_score=kwargs['starbucks_score'],
        lottecinema_score=kwargs['lottecinema_score'],
        megabox_score=kwargs['megabox_score'],
        cgv_score=kwargs['cgv_score'],
        total_score=kwargs['total_score'],
        high_oil=kwargs['high_oil'],
        oil=kwargs['oil'],
        oil2=kwargs['oil2'],
        total=kwargs['total'],
        catch=kwargs['catch'],
        percent=kwargs['percent'],
        mac_count=kwargs['mac_count'],
        lot_count=kwargs['lot_count'],
        burgerking_count=kwargs['burgerking_count'],
        seveneleven_count=kwargs['seveneleven_count'],
        cu_count=kwargs['cu_count'],
        gs25_count=kwargs['gs25_count'],
        starbucks_count=kwargs['starbucks_count'],
        lottecinema_count=kwargs['lottecinema_count'],
        megabox_count=kwargs['megabox_count'],
        cgv_count=kwargs['cgv_count'],
        total_count=kwargs['total_count'],
    )
    return totaladd