from rest_framework import serializers
from .models import Establishment


class AllEstablishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
