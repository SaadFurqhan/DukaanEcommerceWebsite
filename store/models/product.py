from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=800, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    offer = models.BooleanField(default=False)
    offerPercentage = models.IntegerField(default=0,blank=True)
    mrp = models.IntegerField(default=0)
    rating = models.FloatField(default=0)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products_by_search(search):
        return Product.objects.filter(name__contains=search)
    
    @staticmethod
    def get_all_products_by_searchWithCategory(category_id,search):
        return Product.objects.filter(name__contains=search, category = category_id)
    @staticmethod
    def get_all_products_by_category(category_id):
        return Product.objects.filter(category = category_id)[:4]

    @staticmethod
    def get_all_products():
        return Product.objects.all().order_by('category')
    
    @staticmethod
    def get_all_products_by_pricefilter():
        return Product.objects.all().order_by('price')

    @staticmethod
    def get_all_products_by_ratingfilter():
        return Product.objects.all().order_by('-rating')

    @staticmethod
    def get_all_products_by_ratingfilterWithCategory(category_id):
        return Product.objects.filter(category=category_id).order_by('-rating')

    @staticmethod
    def get_all_products_by_pricefilterWithCategory(category_id):
        return Product.objects.filter(category=category_id).order_by('price')
    
    @staticmethod
    def get_products_by_productid(productid):
        return Product.objects.filter(id=productid)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();