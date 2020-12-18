from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):

        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        
        a = []
        
        for o in orders:
            a.append(o.orderId)
            
        orderId = list(dict.fromkeys(a))

       
        filteredObject = []
        for val in orderId:
            filteredObject.append(Order.get_allorders_by_order_id(val))
       

        
        
        data = {}
        data['orders'] = orders
        data['orderIds'] = orderId
        data['filteredObjects'] = set(filteredObject)
        
        return render(request , 'orders.html'  , data)
