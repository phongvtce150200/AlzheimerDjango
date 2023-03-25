from django.db import models

# Create your models here.

class PredictionModel(models.Model):
    image = models.ImageField(upload_to="prediction_images")


class PredictionResult(models.Model):

    prediction_request = models.OneToOneField(to=PredictionModel, related_name="result")


class PredictionResultItem(models.Model):

    result = models.ForeignKey(to=PredictionResult, related_name="items")
    label = models.CharField(max_length=255)
    percentage = models.FloatField()

