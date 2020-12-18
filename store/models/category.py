from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_categoryid(names):
        return Category.objects.filter(name=names)

    def __str__(self):
        return self.name
