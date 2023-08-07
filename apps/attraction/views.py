from django.shortcuts import render

from apps.attraction.models import Attraction, Image_Attraction
from utils.help_model import ProductHelp


# Create your views here.

attractions= Attraction.objects.all() # get all attractions exit

def Attraction(request):
    
    template_name='attraction.html'
    img_attr=Image_Attraction.objects.all()
    att_help=ProductHelp
    attr_list=[]
    for att in attractions:
        
        for img in list(img_attr):
            if att == img.model:
                att_help.image=img.image.url
                att_help.model = att
                attr_list.append(att_help)
    
    
                
    
    
    
    return render(request, template_name, {"attractions": attr_list, 'attr':'active'} )
