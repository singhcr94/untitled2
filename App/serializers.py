from rest_framework import serializers
from .models import person

class personserializers(serializers.ModelSerializer):
    class Meta:
        model= person
        fields=('firstname','lastname','dob','phone','address')