from django.db import models
from core_app.models import BaseModel, User

# Create your models here.
class Farm_info(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50, default=None, blank=True)
    moisture = models.IntegerField(blank=True)
    temperature = models.IntegerField(blank=True)
    light_intensity = models.IntegerField(blank=True)
    humidity = models.IntegerField(blank=True)
    soil_ph = models.IntegerField(blank=True)

