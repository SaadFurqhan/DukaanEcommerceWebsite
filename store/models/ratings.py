from django.db import models
from .product import Product
from .customer import Customer
import datetime


class UserRating(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    feedbackRating = models.FloatField(default=0)

    def saveRating(self):
        self.save()
    
    def productName(self):
        return self.product.name
    
    def customerName(self):
        return self.customer.first_name.capitalize() + ' ' + self.customer.last_name.capitalize()
    

    @staticmethod
    def find_customer_rated_before(c,p):
        return UserRating.objects.filter(customer__id=c,product__id=p)
    