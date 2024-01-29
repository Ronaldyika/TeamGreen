from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    '''
       author: christian
       description: This model will be inherited by all the models
    '''
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField()
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    modified_at = models.DateField(auto_now=False, auto_now_add=False)


class Updates(BaseModel):
    '''
    author: christian
    description: This model stores information about world updates concerned by
    Agriculture and Farming
    '''
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')  # Adjusted path to a subdirectory
    message = models.TextField()  # Changed from CharField to TextField for potentially longer text
    date_added = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return self.title

class Area(BaseModel):
    '''
       author: christian
       description: The Area stores the different areas found in Agriculture e.g Plants..
    '''
    name = models.CharField(max_length=50)

class Categories(BaseModel):
    '''
       author: christian
       description: The categories are under the areas e.g Beans, Livestock
    '''
    area_id = models.ForeignKey("Area",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    tuto_url = models.URLField(max_length=500)


class TutorialPoint(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/')
    link = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.title
    