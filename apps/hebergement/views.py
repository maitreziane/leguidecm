from django.shortcuts import render
from apps.hebergement.models import hebergement, Images_Hebergement
from utils.help_model import ProductHelp
# Create your views here.

def Hebergement_view(request):
    template_name= 'hebergment.html'
    context = {}
    heber_list=[]
    heber=hebergement.objects.all()
    img_heber= Images_Hebergement.objects.all()
    heberhelper=ProductHelp
    id=0
    for heb in list (heber):
        
        for imag_heber in list(img_heber):
            if heb.id == imag_heber.model_id:
                print('enter 3', type(heb.id ))
                heberhelper.model= heb
                heberhelper.image= imag_heber.image.url 
                heber_list.append(heberhelper)
                break
                
                
                
            
            
                
                
            
    context['Hebergement']= heber_list
    context['heber']= 'active'
    
    return render(request, template_name, context)
