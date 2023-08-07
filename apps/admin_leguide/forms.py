from django.forms import ModelForm

from apps.product.models import Product

class add_productForm(ModelForm):
    
    class Meta:
        model=Product
        fields=['title', 'category', 'ville',  'price','descript']