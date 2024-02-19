from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from .forms import Productforms


Product = apps.get_model('proactivehome', 'Product')
Product_modified = apps.get_model('proactivehome', 'Product_modified')
ProductImages = apps.get_model('proactivehome', 'ProductImages')
# Create your views here.


def index(request):
    if request.user.is_authenticated and request.user.verifier:
        uploaded_products = []
        verified_products = []
        products = Product.objects.all()
        products_modifed = Product_modified.objects.all()
        for product in products:
            if products_modifed.get(product_pk = product.id).verified_product == True:
                verified_products.append(product)
            if products_modifed.get(product_pk = product.id).verified_product == False:
                uploaded_products.append(product)
        productscount = products.count()
        uploadedproductcount = len(uploaded_products)
        verifiedproductcount = len(verified_products)
        return render(request, 'verify/index.html', {'products': uploaded_products,'uploadedproductcount' : uploadedproductcount, 'verifiedproductcount' : verifiedproductcount, 'productscount':productscount})
    else:
        return redirect('/accounts/verifiersignin')


def products(request):
    if request.user.is_authenticated and request.user.verifier:
        products = Product.objects.all() 
        products_modifed = Product_modified.objects.all()
        dates_uploaded = []
        
        products_sorted_by_date = {}
        
        for product in products:
            if products_modifed.get(product_pk = product.pk).verified_product != True:
                date =  products_modifed.get(product_pk = product.pk).uploaded_date
                if date not in  dates_uploaded:

                    dates_uploaded.append(date)

        for date_uploaded in dates_uploaded:
            print(date_uploaded)
            products_uploaded = []
            for product in products:
                if products_modifed.get(product_pk = product.pk).uploaded_date == date_uploaded and products_modifed.get(product_pk = product.pk).verified_product == False:
                    print(product)
                    products_uploaded.append(product)
            products_sorted_by_date[str(date_uploaded)] = products_uploaded  

        print(products_sorted_by_date)
        for x in products_sorted_by_date:
            print(products_sorted_by_date[x])
            for y in products_sorted_by_date[x]:
                print(y)
            
            

        return render(request, 'verify/product.html', {'products_sorted_by_date': products_sorted_by_date})
    else:
        return redirect('/accounts/verifiersignin')


def details(request, id):
    if request.user.is_authenticated and request.method == 'POST' and request.user.verifier:
        product_details = Product.objects.get(id=id)
        product_details1 = Product_modified.objects.get(product_pk=id)
        product_details1.verified_product = True
        product_details1.save()
        flag = True
        return render(request, 'verify/details.html', {"details": product_details, "isverified": flag})
    if request.user.is_authenticated and request.method != 'POST':
        product_details = Product.objects.get(id=id)
        flag = False
        return render(request, 'verify/details.html', {"details": product_details, "isverified": flag})
    else:
        return redirect('/accounts/verifiersignin')

# def verifyproduct(request, id):
#     if request.user.is_authenticated:
#         product_details = Product.objects.get(id=id)
#         product_details1 = Product_modified.objects.get(id=id)
#         product_details1.verified_product = True
#         product_details1.save()
#         return render(request, 'verify/details.html', {"details": product_details})
    
#     else:
#         return redirect('/accounts/verifiersignin')


def edit(request, id):
    if request.method == 'POST' and request.user.is_authenticated and request.user.verifier:
        Updateproduct = Product.objects.get(id=id)
        images = request.FILES.getlist('product_image')
        fs = FileSystemStorage(location = '/media/productImages')
        if images != None:
            for image in images:
                fs.save(image.name, image)
                photo = ProductImages.objects.create(product= Updateproduct, image=image )
                
        form = Productforms(request.POST, instance=Updateproduct)
        print("updating................................")
        if form.is_valid():
            print('data is valid')
            form.save()
            images = ProductImages.objects.filter(product = Updateproduct)
            messages.success(request, 'Product Updated successfully')
            return render(request, 'verify/edit.html', {"details": Updateproduct, "images" : images})

    if request.user.is_authenticated and request.user.verifier:
        product_details = Product.objects.get(id=id)
        images = ProductImages.objects.filter(product = product_details )
        return render(request, 'verify/edit.html', {"details": product_details, "images" : images})
    else:
        return redirect('/accounts/verifiersignin')


def delete(request, id):
    if request.user.is_authenticated and request.user.verifier:
        product_details = Product.objects.get(id=id)
        product_details.delete()
        return redirect('verifierproducts')

    else:
        return redirect('/accounts/verifiersignin')

def imageView(request, id):
    if request.user.is_authenticated and request.user.verifier:
        product = get_object_or_404(Product, id=id)
        images = ProductImages.objects.filter(product = product)
        
        return render(request, 'verify/imageviewer.html', {"product": product, "images" :images} )
    else:
        return redirect('/accounts/verifiersignin')