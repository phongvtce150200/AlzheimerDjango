from django.contrib import admin

from .models import MechineLearningModel, Activation


# Register your models here.
@admin.register(MechineLearningModel)
class MechineLearningModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Activation)
class ActivationAdmin(admin.ModelAdmin):
    ...
