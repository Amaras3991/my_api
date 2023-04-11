from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from .models import Smartphone


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ('__all__')

