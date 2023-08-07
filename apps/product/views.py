from django.shortcuts import render
from apps.product.models import Product, Images, Category_product
from utils.help_model import ProductHelp
# Create your views here.



def Product_view(request):
     
    template_name='product.html'
    context = {}
    prod_list=[]
    product=Product.objects.all()
    img_prod= Images.objects.all()
    id_prod  = int
    
        
    for imag_prod in list(img_prod):
        if imag_prod.model_id == id_prod:
            pass
        else:
            print('enter 3',imag_prod.model_id, imag_prod.model.title,imag_prod.image )
            prod_list.append(imag_prod)
        id_prod = imag_prod.model_id
                
                
    context['category']= Category_product.objects.all()          
            
                    
    context['Products']= prod_list
    context['prod']= 'active'
    
    return render(request, template_name, context)