from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    # Create a cart object based on the current session
    cart = Cart(request)
    # Retrieve the product with the given product_id from the database
    product = get_object_or_404(Product, id=product_id)
    # Create a form instance based on the submitted data
    form = CartAddProductForm(request.POST)
    
    # Check if the form is valid
    if form.is_valid():
        # Get the cleaned data from the form
        cd = form.cleaned_data
        # Add the product to the cart
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        # Redirect to the cart detail page
        return redirect('cart:cart_detail')

    # If the form is not valid, render the product detail page with the form and product
    return render(request, 'shop/product/detail.html', {'product': product, 'form': form})
def cart_remove(request, product_id):
    # Create a cart object based on the current session
    cart = Cart(request)
    # Retrieve the product with the given product_id from the database
    product = get_object_or_404(Product, id=product_id)
    # Remove the product from the cart
    cart.remove(product)
    # Redirect to the cart detail page
    return redirect('cart:cart_detail')


def cart_detail(request):
 cart = Cart(request)
 return render(request, 'cart/detail.html', {'cart': cart})