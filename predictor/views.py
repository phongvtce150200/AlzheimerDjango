
from .serializers import PredictionModelSerializer
from rest_framework import viewsets
from .models import PredictionModel


class PredictionModelViewSet(viewsets.ModelViewSet):
    queryset = PredictionModel.objects.all()
    serializer_class = PredictionModelSerializer
