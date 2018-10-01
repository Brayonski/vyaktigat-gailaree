from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    location =  models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to= 'media/')
    image_name = models.CharField(max_length=50)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    @classmethod
    def all_snaps(cls):
        today = dt.date.today()
        snaps = cls.objects.filter(pub_date_date = today)
        return snaps
        
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
    @classmethod
    def search_by_image(cls,search_term):
        snaps = cls.objects.filter(category__category__icontains=search_term)
        return snaps
    
    def filter_by_location(cls,filter_term):
        snaps = cls.objects.filter(image_icontains=filter_term)

    
    
