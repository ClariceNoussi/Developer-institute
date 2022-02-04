from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddProductForm
from .models import Products
from django.views import generic
from django.shortcuts import render


def produits(request):
    all_products= Products.objects.all() #query to get all the animals instances in my Animals table
    if request.method == 'POST': #necessary to get data from the user
        #We are inside the post http method
        print('in_post')
        #we fetch the user search with the value of the input's atribute name (animal-searcg)
        search_result = request.POST.get('product-search')
        print(search_result)
        #we filter animals instances that corresponds to the user searc text
        product_searched = Products.objects.filter(name__contains=search_result.title())
        return render(request, 'product.html', {'products': product_searched,
                                             'search': search_result} )
    return render(request, 'products.html', {'products':
                                         all_products})


def product(request, product_id):

    product = get_object_or_404(Products, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def add_product(request):
    if request.method == 'POST':
        print('in post')
        add_form = AddProductForm(request.POST, request.FILES)
        if add_form.is_valid():
            print('in valid')
            new_product = add_form.save() #we can use the save method directly on the form because it comes from modelForm and it creates a new animal instance
            messages.success(request, f'New Product {new_product.name} saved')
            return redirect('products')
    else:
        add_form = AddProductForm()
        return render(request, 'add_product.html', {'form_a':add_form})


def buy(request, id):
    product = Products.objects.get(id=id) #first we get the product the user wants to buy
    product.owner.set([request.user]) # we set the current user to be the owner of this product
    messages.success(request, 'product successfully add to your shopping cart')
    return redirect('home')


def show_panier(request):
    #we want to filter all the animals owned by the current user
    products_inside_cart = Products.objects.filter(owner=request.user)
    return render(request, 'products.html', {'Products': products_inside_cart})