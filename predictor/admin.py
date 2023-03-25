from django.contrib import admin
from .models import PredictionModel, PredictionResult, PredictionResultItem


# Register your models here.
@admin.register(PredictionModel)
class PredictionModelAdmin(admin.ModelAdmin):
    ...
