from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from apps.users.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
# Create your views here.


def Register(request):
    
    template_name= 'register.html'
    context = {}
    
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            
            return redirect ('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    
		    
    return render(request, template_name,context)


def Login(request):
    
    template_name= 'login.html'
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("index")
    else:
        form = AccountAuthenticationForm()
		

    context['login_form'] = form
				
    return render(request, template_name, context)


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def Profil(request):
    
    user = request.user
    if user.is_authenticated:
        
        
    
    
        return render(request,'profil.html')
