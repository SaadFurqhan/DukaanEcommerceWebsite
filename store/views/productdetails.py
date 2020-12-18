from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.contrib import messages
from store.models.product import Product
from store.models.orders import Order
from store.models.ratings import UserRating
from store.middlewares.auth import auth_middleware

class ProductView(View):
    def post(self , request):
            existingRating = 0
            ratedBefore = False
            userRatings = request.POST.get('ratings')
            customer = request.session.get('customer')
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if userRatings == None:
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
                        messages.success(request,'Item is added to cart!')
                else:
                    cart = {}
                    cart[product] = 1
                    messages.success(request,'Item is added to cart!')

            request.session['cart'] = cart
            product = Product.get_products_by_productid(product)
            for products in product:
                category = products.category
                existingRating = products.rating
            
            if userRatings:
                newRating = (existingRating+float(userRatings))/2
                print(newRating)
                for p in product:
                    rating = UserRating(customer=Customer(id=customer),
                                    product=p,
                                    feedbackRating=userRatings
                                    )
                    rating.saveRating()
                    p.rating = newRating
                    p.save()
                ratedBefore = True
                
            
        
            categories = Product.get_all_products_by_category(category)
            data = {}
            data['products'] = product
            data['categories'] = categories
            data['ratedBefore'] = ratedBefore
            return render(request , 'productdetails.html'  , data)
            


    def get(self , request ):
        ratedBefore = False
        customer = request.session.get('customer')
        productid = request.GET.get('productid')
        product = Product.get_products_by_productid(productid)
        for products in product:
            category = products.category
        categories = Product.get_all_products_by_category(category)

       
        check_rated = UserRating.find_customer_rated_before(customer,productid)
        if check_rated:
            ratedBefore = True
        
        data = {}
        data['products'] = product
        data['categories'] = categories
        data['ratedBefore'] = ratedBefore
        return render(request , 'productdetails.html'  , data)

