from .models import *
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalAddress
        fields = ('id', 'address','gu', 'dong', 'mac_score', 'lot_score', 'burgerking_score', 'seveneleven_score', 'cu_score',
                  'gs25_score', 'starbucks_score', 'lottecinema_score', 'megabox_score', 'cgv_score', 'total_score',
                  'high_oil', 'oil', 'oil2', 'total', 'catch', 'percent', 'mac_count', 'lot_count', 'burgerking_count', 'seveneleven_count', 'cu_count', 'gs25_count', 'starbucks_count', 'lottecinema_count',
                  'megabox_count', 'cgv_count', 'total_count', 'first', 'second', 'third', 'first_mapx', 'first_mapy', 'second_mapx', 'second_mapy', 'third_mapx', 'third_mapy', 'elementary_count', 'middle_count',
                  'high_count','park_count','station')
