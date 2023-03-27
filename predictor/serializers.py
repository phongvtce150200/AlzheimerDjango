from rest_framework import serializers
from .models import PredictionModel, PredictionResult, PredictionResultItem


class PredictionResultItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionResultItem
        fields = ["label", "percentage"]


class PredictionResultSerializer(serializers.ModelSerializer):
    items = PredictionResultItemSerializer(many=True, read_only=True)

    class Meta:
        model = PredictionResult
        fields = ["id", "items"]


class PredictionModelSerializer(serializers.ModelSerializer):
    result = PredictionResultSerializer(read_only=True)

    class Meta:
        model = PredictionModel
        fields = ["id", "result", "image"]
