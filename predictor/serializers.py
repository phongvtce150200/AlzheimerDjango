from rest_framework import serializers
from .models import PredictionModel, PredictionResult, PredictionResultItem


class PredictionResultItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionResultItem
        fields = "__all__"


class PredictionResultSerializer(serializers.ModelSerializer):
    items = PredictionResultItemSerializer(many=False, read_only=True)

    class Meta:
        model = PredictionResult
        fields = "__all__"


class PredictionModelSerializer(serializers.ModelSerializer):
    result = PredictionResultSerializer(read_only=True)

    class Meta:
        model = PredictionModel
        fields = "__all__"
