from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from .forms import Productforms


Product = apps.get_model('proactivehome', 'Product')
Product_modified = apps.get_model('proactivehome', 'Product_modified')
ProductInMagento = apps.get_model('proactivehome', 'ProductInMagento')
ProductImages = apps.get_model('proactivehome', 'ProductImages')
ProductInMagentoImages = apps.get_model('proactivehome', 'ProductInMagentoImages')
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        uploaded_products = []
        verified_products = []
        products = Product.objects.all()
        products_modifed = Product_modified.objects.all()
        productInMagento = ProductInMagento.objects.all()
        for product in products:
            if products_modifed.get(product_pk = product.id).verified_product == True and products_modifed.get(product_pk = product.id).uploaded_product_magento == False:
                verified_products.append(product)
            if products_modifed.get(product_pk = product.id).verified_product == False and products_modifed.get(product_pk = product.id).uploaded_product_magento == False:
                uploaded_products.append(product)
        productscount = products.count()
        uploadedproductcount = len(uploaded_products)
        verifiedproductcount = len(verified_products)
        return render(request, 'view/index.html', {'products': products, 'productInMagento' : productInMagento ,'uploadedproductcount' : uploadedproductcount, 'verifiedproductcount' : verifiedproductcount, 'productscount':productscount, 'uploaded_products' : uploaded_products, 'verified_products': verified_products})
    else:
        return redirect('/accounts/viewersignin')


def products(request):
    if request.user.is_authenticated:   
        uploaded_products = []
        verified_products = []
        products = Product.objects.all()
        products_modifed = Product_modified.objects.all()
        for product in products:
            if products_modifed.get(product_pk = product.id).verified_product == True and products_modifed.get(product_pk = product.id).uploaded_product_magento == False :
                verified_products.append(product)
            if products_modifed.get(product_pk = product.id).verified_product == False and products_modifed.get(product_pk = product.id).uploaded_product_magento == False:
                uploaded_products.append(product)
        # productscount = products.count()
        # uploadedproductcount = len(uploaded_products)
        # verifiedproductcount = len(verified_products)
        return render(request, 'view/product.html', {'products': products, 'uploaded_products' : uploaded_products, 'verified_products': verified_products})
    else:
        return redirect('/accounts/viewersignin')

def details(request, id):
    if request.user.is_authenticated and request.method == 'POST':
        product_details = Product.objects.get(id=id)
        product_details1 = Product_modified.objects.get(product_pk=id)
        product_details1.uploaded_product_magento = True
        product_details1.save()
        # myfile = request.FILES[product_details.product_image]
        # fs = FileSystemStorage(location = '/media/mproductImages')
        # fs.save(myfile.name, myfile)
        saverecord = ProductInMagento()
        saverecord.mmagento_id = request.POST.get('mmagento_id')
        saverecord.mproduct_id = product_details.product_id
        saverecord.mlocation_id = product_details.location_id
        saverecord.mbuilding = product_details.building
        saverecord.mfloor = product_details.floor
        saverecord.munit = product_details.unit
        saverecord.mrow = product_details.row
        saverecord.mcolumn = product_details.column
        saverecord.mpallet = product_details.pallet
        saverecord.mlevel = product_details.level
        saverecord.mdimension = product_details.dimension
        saverecord.mweight = product_details.weight
        saverecord.mdescription = product_details.description
        saverecord.mquantity = product_details.quantity
        saverecord.mmake_brand = product_details.make_brand
        saverecord.msource = product_details.source
        saverecord.mprice = product_details.price
        saverecord.mproduct_link = product_details.product_link
        saverecord.save()
        
        currentMProduct = ProductInMagento.objects.get(id=saverecord.id)
        print('***********************')
        productimages = ProductImages.objects.filter(product = product_details)
        print(productimages)
        if productimages != None:
            for productimage in productimages:
                photo = ProductInMagentoImages.objects.create(mproduct = currentMProduct,mimage = productimage.image)
        

        flag = True
        return render(request, 'view/details.html', {"details": product_details, "isupdated": flag})
    if request.user.is_authenticated and request.method != 'POST':
        product_details = Product.objects.get(id=id)

        verifiedFlag = Product_modified.objects.get(product_pk = product_details).verified_product

        flag = False
        return render(request, 'view/details.html', {"details": product_details, "isupdated": flag, "verifiedFlag" : verifiedFlag})
    else:
        return redirect('/accounts/viewersignin')


def edit(request, id):
    if request.method == 'POST' and request.user.is_authenticated and request.user.viewer:
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
            return render(request, 'view/edit.html', {"details": Updateproduct, "images" : images})

    if request.user.is_authenticated and request.user.viewer:
        product_details = Product.objects.get(id=id)
        images = ProductImages.objects.filter(product = product_details )
        return render(request, 'view/edit.html', {"details": product_details, "images" : images})
    else:
        return redirect('/accounts/viewersignin')

def delete(request, id):
    if request.user.is_authenticated:
        product_details = Product.objects.get(id=id)
        product_details.delete()
        return redirect('viewerproducts')

    else:
        return redirect('/accounts/viewersignin')

def remove(request, id):
    if request.user.is_authenticated:
        product_details = ProductInMagento.objects.get(id=id)
        product_details.delete()
        return redirect('viewermagentoproducts')

    else:
        return redirect('/accounts/viewersignin')


def magentoproducts(request):
    if request.user.is_authenticated and request.method != 'POST':
        product_details = ProductInMagento.objects.all()

        return render(request, 'view/magento.html', {"products" : product_details })
    else:
        return redirect('/accounts/viewersignin')

def imageView(request, id):
    if request.user.is_authenticated and request.user.viewer:
        product = get_object_or_404(Product, id=id)
        images = ProductImages.objects.filter(product = product)
        
        return render(request, 'view/imageviewer.html', {"product": product, "images" :images} )
    else:
        return redirect('/accounts/viewersignin')

