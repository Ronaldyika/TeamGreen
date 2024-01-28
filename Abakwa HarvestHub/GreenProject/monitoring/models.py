from django.db import models
from core_app.models import BaseModel, User

# Create your models here.
class Farm_info(BaseModel):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    moisture = models.IntegerField()
    temperature = models.IntegerField()
    light_intensity = models.IntegerField()
    humidity = models.IntegerField()
    soil_ph = models.IntegerField()
