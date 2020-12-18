from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class AllOrders(View):
    def post(self,request):
       
        options = request.POST.get('option')
        search = request.POST.get('search')
        if options == "date":
            orders = Order.get_orders_by_date(search)
        elif options == "orderID":
            orders = Order.get_allorders_by_orderid(search)
        elif search == "":
            orders = Order.get_allorders()
        a = []
        
        for o in orders:
            a.append(o.orderId)
            
        orderId = set(a)

       
        filteredObject = []
        for val in orderId:
            filteredObject.append(Order.get_allorders_by_order_id(val))
       
       
        data = {}
        data['orders'] = orders
        data['orderIds'] = orderId
        data['filteredObjects'] = set(filteredObject)
        
        
        
        return render(request , 'allorders.html'  , data)

    def get(self , request):
        orders = Order.get_allorders()
        
        a = []
        
        for o in orders:
            a.append(o.orderId)
            
        orderId = set(a)

       
        filteredObject = []
        for val in orderId:
            filteredObject.append(Order.get_allorders_by_order_id(val))
       
        
        data = {}
        data['orders'] = orders
        data['orderIds'] = orderId
        data['filteredObjects'] = set(filteredObject)
        
        
        
        return render(request , 'allorders.html'  , data)
