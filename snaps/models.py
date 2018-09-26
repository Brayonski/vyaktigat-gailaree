from django.db import models
import datetime as dt
# Create your models here.

class Image(models):
    image = models.ImageField(upload_to = 'category/', default='DEFAULT IMAGE')
    image_name = models.TextField()
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
    
    def search_by_category(cls,search_term):
        snaps = cls.object.filter(image_icontains=search_term)
    
    def filter_by_location(cls,filter_term):
        snaps = cls.object.filter(image_icontains=filter_term)
    
class Location(models.Model):
    location =  models.TextField()

    def __str__(self):
        return self.location

    def __str__(self):
        return self.location

class Meta:
    ordering = ['location']

class Category(models.Model):
    category = models.TextField(Image)

