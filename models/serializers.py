from rest_framework import serializers
from models.models import shool

class shool_serializer(serializers.ModelSerializer):
    class Meta:
        model = shool
        fields = 'name', 'city', 'street', 'country', 'school_type'



