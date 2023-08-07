from django.shortcuts import render, get_object_or_404

from apps.attraction.models import Attraction
from apps.product.models import Images, Product
from apps.attraction.models import Attraction, Image_Attraction
from utils.help_model import ProductHelp

# Create your views here.
attractions= Attraction.objects.all() # get all attractions exit

def Index(request):
    
    attr_pop= Attraction.objects.all()
    
    template_name='index.html'
    
    context = {}
    
   
    context["attr_pop"]=attr_pop
    prod_list=[]
    img_prod= Images.objects.all()
    img_attr=Image_Attraction.objects.all()
    id_prod  = int
    
        
    for imag_prod in list(img_prod):
        if imag_prod.model_id == id_prod:
            pass
        else:
            print('enter 3',imag_prod.model_id, imag_prod.model.title,imag_prod.image )
            prod_list.append(imag_prod)
        id_prod = imag_prod.model_id
                
            
                    
    context['products']= prod_list
    
    
    
    att_help=ProductHelp
    attr_list=[]
    for att in attractions:
        
        for img in list(img_attr):
            if att == img.model:
                att_help.image=img.image.url
                att_help.model = att
                attr_list.append(att_help)
    context['attractions']= attr_list
    context['home']= 'active'
    
    return render(request,template_name, context)


def About(request):
    context= {}
    context['about']= 'active'
    return render(request, 'about.html', context)



template_name='detail.html'

def detailProduct(request, category_slug,id):
    
    
    
    print(id , category_slug)
    
    product = get_object_or_404(Product, id=int(id))
    
    
    
    return render(request, template_name)