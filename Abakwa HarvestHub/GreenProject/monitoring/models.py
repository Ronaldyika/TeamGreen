from django.db import models
from core_app.models import BaseModel, User

# Create your models here.
class Farm_info(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    name = models.CharField(max_length=30 , default='Famer1')
    moisture = models.IntegerField(null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)
    light_intensity = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    soil_ph = models.IntegerField(null=True, blank=True)



