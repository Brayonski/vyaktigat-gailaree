from django.db import models
import datetime as dt
# Create your models here.

class Image(models):
    image = models.ImageField(upload_to = 'category/', default='DEFAULT IMAGE')
    image_name = models.TextField()
    description = models.TextField()

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
    
    

