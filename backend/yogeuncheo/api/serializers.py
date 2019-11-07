from .models import *
from rest_framework import serializers
# @property
# seen_movies_id = serializers.SerializerMethodField('get_movielist_id')


class ApartmentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    location = serializers.SerializerMethodField('get_location')

    class Meta:
        model = Apartment
        fields = ('id', 'name', 'location')

    def get_location(self, obj):
        return obj.location.name

