from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from producto.models import Producto
from producto.form import ProductoForm
# Create your views here.

def Products(request):
    return render(request, 'home.html')

def ListProducts(request):
    products = Producto.objects.all()
    context = {'products': products}
    return render(request, 'tienda.html', context)

def CreateProduct(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponse('Gracias!!!')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductoForm()
    return render(request, 'registerProduct.html', {'form': form})
    #return render(request, 'name.html', )
    



def UpdateProduct(request):
    return HttpResponse('Aca se actualizaran los productos existentes')

def ProductOwner(request):
    return HttpResponse('Aca se le añadiran cuentas de cliente al producto')