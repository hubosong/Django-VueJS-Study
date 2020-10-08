from rest_framework import serializers
from . models import Pictures

class PicturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pictures
        fields = '__all__'