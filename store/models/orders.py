from django.db import models
from .product import Product
from .customer import Customer
import datetime

STATUS_CHOICE = [
    ('c',True),
    ('p',False),
]

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False,choices=STATUS_CHOICE)
    grandtotal = models.IntegerField()
    orderId = models.IntegerField()

    def placeOrder(self):
        self.save()
    
    def productName(self):
        return self.product.name
    
    def customerName(self):
        return self.customer.first_name.capitalize() + ' ' + self.customer.last_name.capitalize()
    
    def customerPhone(self):
        return self.customer.phone
    
    def statusConditions(self):
        return self.status

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    @staticmethod
    def get_orders_by_date(date):
        return Order.objects.filter(date=date).order_by('-date')
    @staticmethod
    def get_allorders():
        return Order.objects.all().order_by('date')

    @staticmethod
    def get_allorders_by_orderid(orderid):
        return Order.objects.filter(orderId=orderid)
    @staticmethod
    def get_allorders_by_order_id(order_id):
        return Order.objects.filter(orderId=order_id)[:1]
