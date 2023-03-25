from django.shortcuts import render
from .serializers import MechineLearningModelSerializer, ActivationSerializer
from .models import MechineLearningModel, Activation

from rest_framework import viewsets

class MechineLearningModelViewSet(viewsets.ModelViewSet):
    serializer_class = MechineLearningModelSerializer
    queryset = MechineLearningModel.objects.all()


class ActivationViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.all()
