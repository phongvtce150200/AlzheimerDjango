from .models import PredictionModel, PredictionResult, PredictionResultItem
from django.db.models.signals import post_save
from django.dispatch import receiver

from .processor import predict


@receiver(post_save, sender=PredictionModel)
def create_prediction_result(sender, instance, created, **kwargs):
    if created:
        result = PredictionResult.objects.create(prediction_request=instance)
        image_path = instance.image.path

        predict_result = predict(image_path)
        for label, acc in predict_result.items():
            result_item = PredictionResultItem.objects.create(
                result=result, label=label, percentage=acc
            )
