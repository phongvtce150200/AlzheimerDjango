from django.db import models


# Create your models here.
class MechineLearningModel(models.Model):
    file = models.FileField(upload_to="meachine_learning_models")
    name = models.CharField(max_length=255)
    acc = models.FloatField(default=0)

    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.acc} %"


class Activation(models.Model):
    model = models.ForeignKey(to=MechineLearningModel, on_delete=models.CASCADE)
    active_at = models.DateTimeField(auto_now_add=True)
