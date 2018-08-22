from rest_framework import serializers
from .models import Establishment


class AllEstablishSerializer(serializers.ModelSerializer):
    get_category_display = serializers.ReadOnlyField()

    class Meta:
        model = Establishment
        fields = '__all__'
