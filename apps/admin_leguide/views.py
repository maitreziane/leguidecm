from django.shortcuts import render, redirect
from apps.admin_leguide.forms import add_productForm
from apps.product.models import Product, Category_product, Images
from apps.attraction.models import *
from apps.hebergement.models import *

# Create your views here.


def StartIndex_admin(request):
    
    template_name= 'start_manage.html'
    
    
    return render (request, template_name)


def add_product(request):
    
    template_name='add_product.html'
    category_pro=''
    context = {}
    user = request.user
    '''if not user.is_authenticated:
        return redirect('must_authenticate')'''
    
    context['category']=Category_product.objects.all()
    if request.POST:
        for category in list(Category_product.objects.all()):
        
            if category.category_name in request.POST.get('category'):
                
                product_add= Product.objects.create(title=request.POST.get('title'),days=request.POST.get('days'),category=category,ville=request.POST.get('ville'),price= request.POST.get('price'),descript=request.POST.get('descript') )
                product_add.save()
                
                if request.FILES:
                    
                    for file in request.FILES.getlist('image'):
                        img_prod= Images.objects.create(model=product_add, image=file)
                        img_prod.save()
        
   


    return render(request, template_name, context )


def add_attraction(request):
    
    template_name= 'add_attraction.html'
    context = {}
    user = request.user
    '''if not user.is_authenticated:
        return redirect('must_authenticate')'''
    
    print(request.POST)
    
    context['category']=Category_attraction.objects.all()
    if request.POST:
        for category in list(Category_attraction.objects.all()):
        
            if category.type_attr in request.POST.get('category'):
                
                attr_add= Attraction.objects.create(title=request.POST.get('title'),category=category,ville=request.POST.get('ville'),descript=request.POST.get('descript') )
                attr_add.save()
                for f in request.FILES.getlist('image'):
                    img_att= Image_Attraction.objects.create(model=attr_add, image=f)
                    img_att.save()
        print(Attraction.objects.all())
    
    return render(request, template_name, context )

def add_hebergement(request):
    
    template_name= 'add_hebergement.html'
    
    print(request.POST, request.FILES)
    
    if request.POST:
        
        pass
                
        heber_add= hebergement.objects.create(name_heb=request.POST.get('name'),localisation=request.POST.get('ville'),nb_star=request.POST.get('star'), contact=request.POST.get('contact'))
        heber_add.save()
        for f in request.FILES.getlist('image'):
            img_att= Images_Hebergement.objects.create(model=heber_add, image=f)
            img_att.save()
        print(hebergement.objects.all())
    
    return render(request, template_name )
