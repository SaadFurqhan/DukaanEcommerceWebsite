from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def post(self , request):
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                            messages.warning(request,'Item is removed from cart!')
                        else:
                            cart[product]  = quantity-1
                            messages.warning(request,'Item quantity is deducted from cart!')
                    else:
                        cart[product]  = quantity+1
                        messages.success(request,'Item quantity is updated in cart!')
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1


            request.session['cart'] = cart 
            return redirect('cart')

    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request , 'cart.html' , {'products' : products} )

