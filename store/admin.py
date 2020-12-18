from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.ratings import UserRating

def update_status(modeladmin,request,queryset):
    queryset.update(status='True')
    update_status.short_description = "Mark selected orders as Completed"
    
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','offer']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']

class AdminOrder(admin.ModelAdmin):
    list_display = ['productName','customerName','customerPhone','quantity','statusConditions']
    actions = [update_status]

class AdminRating(admin.ModelAdmin):
    list_display = ['productName','customerName','feedbackRating']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer, AdminCustomer )
admin.site.register(Order ,AdminOrder)
admin.site.register(UserRating,AdminRating)

