from operator import mod
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField


class Category_attraction(models.Model):
    
    """
        spécifier le type d'attraction ( Parc, chute, mont, musée ...)
        
    """
    
    type_attr= models.CharField(max_length=255, null=False)
    slug_type= models.SlugField(max_length=80, null=False)
    
    
    def __str__(self) -> str:
        return self.type_attr

class Attraction(models.Model):

    category    = models.ForeignKey(Category_attraction, blank=True, on_delete=models.CASCADE, default=1)
    title       = models.CharField(max_length=255, null=False)
    ville       = models.CharField(max_length=255, null=False)
     #phone       = ''
    descript    = RichTextField()
    #thumbnail   = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)


class Image_Attraction(models.Model):
    model       = models.ForeignKey(Attraction, blank=True, on_delete=models.CASCADE, default=1)
    image       = models.ImageField(upload_to="uploads/attraction", blank=True, null=False)
    
    def get_img(self):
        if self.image: return self.image.url
        
    def slug_ville(self): return slugify(self.ville)

