from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.contrib import messages


# Create your views here.
class Index(View):

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
                    messages.success(request,'Item is added to cart!')
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            
            categoryID = None
            categoryNameforDisplay = None
            search = request.POST.get('search')
            cart = request.session.get('cart')
            filtervalue = request.POST.get('filtering')
            categoryName = request.POST.get('categoryBtn')
            currentCategory = request.POST.get('currentCategory')
            
            if categoryName:
                getcategoryID = Category.get_categoryid(categoryName)
                for category in getcategoryID:
                    categoryID = category.id
            if not cart:
                request.session['cart'] = {}
            products = None
            categories = Category.get_all_categories()
            #categoryID = request.GET.get('category')
            if currentCategory != "None" and filtervalue == "price":
                products = Product.get_all_products_by_pricefilterWithCategory(currentCategory)
                categoryNameforDisplay = categoryName
            elif categoryID:
                products = Product.get_all_products_by_categoryid(categoryID)
                currentCategory = categoryID
                categoryNameforDisplay = categoryName
            elif filtervalue == "price":
                products = Product.get_all_products_by_pricefilter()
                currentCategory = categoryID
                categoryNameforDisplay = categoryName
            elif search != None: 
                products = Product.get_all_products_by_search(search)
                currentCategory = categoryID
                categoryNameforDisplay = categoryName
            elif filtervalue == "price":
                products = Product.get_all_products_by_pricefilter()
            else:
                products = Product.get_all_products()

            data = {}
            data['products'] = products
            data['categories'] = categories
            data['currentCategory'] = currentCategory
            data['categoryNameforDisplay'] = categoryNameforDisplay
            return render(request, 'index.html', data)



    def get(self , request):
        # print()
        #return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        
        return render(request,"home.html",data)

def store(request):
    categoryID = None
    categoryNameforDisplay = None
    search = request.POST.get('search')
    cart = request.session.get('cart')
    filtervalue = request.POST.get('filtering')
    categoryName = request.POST.get('categoryBtn')
    currentCategory = request.POST.get('currentCategory')
    
    if categoryName:
        getcategoryID = Category.get_categoryid(categoryName)
        for category in getcategoryID:
            categoryID = category.id
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    #categoryID = request.GET.get('category')
    if currentCategory != "None" and filtervalue == "price":
        products = Product.get_all_products_by_pricefilterWithCategory(currentCategory)
        categoryNameforDisplay = categoryName
    elif currentCategory != "None" and filtervalue == "rating":
        products = Product.get_all_products_by_ratingfilterWithCategory(currentCategory)
        categoryNameforDisplay = categoryName
    elif categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
        currentCategory = categoryID
        categoryNameforDisplay = categoryName
    elif filtervalue == "price":
        products = Product.get_all_products_by_pricefilter()
        currentCategory = categoryID
        categoryNameforDisplay = categoryName
    elif filtervalue == "rating":
        products = Product.get_all_products_by_ratingfilter()
        currentCategory = categoryID
        categoryNameforDisplay = categoryName
    elif search != None: 
        products = Product.get_all_products_by_search(search)
        currentCategory = categoryID
        categoryNameforDisplay = categoryName
    elif filtervalue == "price":
        products = Product.get_all_products_by_pricefilter()
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['currentCategory'] = currentCategory
    data['categoryNameforDisplay'] = categoryNameforDisplay
    return render(request, 'index.html', data)

