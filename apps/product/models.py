from django.db import models

# Create your models here.


class Category_product(models.Model):
    
    """
        #spécifier le type d'un produit( Mini-séjour, Séjour, Circuit ...)
    """
    
    category_name    = models.CharField(max_length=255, null=False)
    slug_type        = models.SlugField(max_length=255, null=False)


class Product (models.Model):
    
    title       = models.CharField(max_length=255, null=False)
    category    = models.ForeignKey(Category_product, blank=True, on_delete=models.CASCADE, default=1)
    ville       = models.CharField(max_length=255, null=False)
    price       = models.CharField(max_length=50, null=False)
    days        = models.CharField( max_length=50, null=False, default=2)
    descript    = models.TextField(max_length=5000,blank=True, null=True)
    '''objectif    = models.TextField(max_length=5000,blank=True, null=True)
    start       = models.CharField(max_length=255, null=True)
    end         = models.CharField(max_length=255, null=True)'''
    # à ajouter (intérêt, start point and end point)
    
    
class Images(models.Model):
    
    model       = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, default=1)
    image       = models.ImageField(upload_to="uploads/product", blank=True, null=False) 
    
    