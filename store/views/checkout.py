from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
import random
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        GrandTotal = int(request.POST.get('GrandTotal'))
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        error_message = None
        error_message = self.validateCustomer(address,phone)

        if not error_message:
            orderID = random.randint(0,9999)
            for product in products:
                order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          grandtotal=GrandTotal,
                          orderId=orderID,
                          quantity=cart.get(str(product.id)))
                order.save()
            request.session['cart'] = {}
            messages.success(request,"Order placed successfully!")
            return redirect('orders')
        else:
            messages.warning(request,error_message)
            return redirect('cart')

    def validateCustomer(self, address,phone):
        error_message = None
        if (not address):
            error_message = "Address required !!"
        elif not phone:
            error_message = 'Phone Number required !!'
        elif len(phone) < 10 or len(phone) > 10:
            error_message = 'Phone Number must be 10 char Long !!'
        return error_message

