from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, ContactForm, CartItem
from .forms import ContactFormForm, ContactFormModelForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

# Create your views here.


def index(request):
    
    flanes_publicos = Flan.objects.filter(is_private=False, is_premium=False)
    context = {'flanes': flanes_publicos}
    return render(request,'web/index.html',context)


def about(request):
    return render(request,'web/about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True, is_premium=False)
    context = {'flanes':flanes_privados}
    return render(request,'web/welcome.html',context)


def contact(request):
    
    if request.method != 'POST':
        form = ContactFormForm()
        context = {'form':form}
        return render(request,'web/contact.html',context)
    else:
        form = ContactFormModelForm()
        try:

            form = ContactFormModelForm(request.POST)
            if form.is_valid():
                #contact_form = ContactForm.objects.create(**form.cleaned_data)
                form.save()
                return redirect('form_success')
            else:
                context = {'form':form}
                return render(request,'web/contact.html',context)
            
        except ValueError:
            context = {'form': form,'error':'Ingresar datos válidos'}
            return render(request,'web/contact.html',context)
        
        

def form_success(request):
    context = {'message':'Gracias por contactarte con OnlyFlans, te responderemos en breve'}
    return render(request,'web/sucess.html',context)




def sign_up(request):
    if request.method == 'GET':
        return render(request, 'web/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('welcome')
            except Exception as e:
                return HttpResponse(str(e))
        return HttpResponse("Las contraseñas no coinciden")


def log_in(request):
    if request.method =='GET':
        return render(request, 'web/login.html',{'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'web/login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña no son correctos.'
            })
        else:
            login(request, user)
            return redirect('welcome')


def sign_out(request):
    
    logout(request)
    return redirect('index')



@login_required  
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'web/cart.html', {'cart_items': cart_items, 'total': total})

@login_required  
def add_to_cart(request, product_id):
    product = get_object_or_404(Flan, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')  

@login_required 
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')  


@login_required
@permission_required('web.can_view_premium', raise_exception=True)
def premium_flan_list(request):
    try:
        premium_flans = Flan.objects.filter(is_premium=True)
        return render(request, 'web/premium_flans.html', {'premium_flans': premium_flans})
    except PermissionDenied:
        return render(request,'web/suscribe.html', status=200)