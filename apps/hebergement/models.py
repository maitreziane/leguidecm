from django.db import models

# Create your models here.

class hebergement(models.Model):
    
    
    name_heb        = models.CharField(max_length=255, null=False)
    localisation    = models.TextField(blank=True, null=True)
    nb_star         = models.IntegerField(default=1)
    contact         = models.CharField(null=True, max_length=50)

class Images_Hebergement(models.Model):
    
    model           = models.ForeignKey(hebergement, blank=True, on_delete=models.CASCADE, default=1)
    image           = models.ImageField(upload_to="uploads/hebergement", blank=True, null=False) 
    
    
    
    