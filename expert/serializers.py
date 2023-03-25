from .models import MechineLearningModel, Activation
from rest_framework import serializers

class MechineLearningModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechineLearningModel
        fields = '__all__'

class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation
        fields = '__all__'
