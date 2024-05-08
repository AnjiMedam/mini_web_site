from rest_framework import serializers
from .models import *

class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactform
        fields='__all__'
