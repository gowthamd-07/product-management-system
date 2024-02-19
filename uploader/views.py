from proactivehome.models import Product_modified
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from .forms import Productforms
#from django.db.models.loading import get_model
# Create your views here.


Product = apps.get_model('proactivehome', 'Product')
Product_modified = apps.get_model('proactivehome', 'Product_modified')
ProductImages = apps.get_model('proactivehome', 'ProductImages')

def index(request):
    if request.user.is_authenticated and request.user.uploader:
        uploaded_products = []
        products = Product.objects.all()
        products_modifed = Product_modified.objects.all()
        for product in products:
            if products_modifed.get(product_pk = product.id).verified_product == False:
                uploaded_products.append(product)
        productcount = len(uploaded_products)
        return render(request, 'upload/index.html', {'products': uploaded_products, 'productcount' : productcount})
    else:
        return redirect( '/accounts/uploadersignin')

def products(request):
    if request.user.is_authenticated and request.user.uploader:
        uploaded_products = []
        products = Product.objects.all()
        products_modifed = Product_modified.objects.all()
        for product in products:
            if products_modifed.get(product_pk = product.id).verified_product == False:
                uploaded_products.append(product)
        productcount = len(uploaded_products)
        
        return render(request, 'upload/product.html', {'products': uploaded_products})
    else:
        return redirect( '/accounts/uploadersignin')

def addProduct(request):
    images = []
    if request.method == 'POST' and request.user.is_authenticated and  request.user.uploader:
        if request.FILES.getlist('product_image'):
            images = request.FILES.getlist('product_image')
            fs = FileSystemStorage(location = '/media/productImages')
            if images != None:
                for image in images:
                    fs.save(image.name, image)

        saverecord = Product()
        saverecordM = Product_modified()
        # if request.POST.get('product_id') or request.POST.get('product_id') == None:
        saverecord.product_id = request.POST.get('product_id')
        # if request.POST.get('location_id'):
        saverecord.location_id = request.POST.get('location_id')
        
        saverecord.building = request.POST.get('building')
        # if request.POST.get('floor'):
        saverecord.floor = request.POST.get('floor')
        # if request.POST.get('unit'):
        saverecord.unit = request.POST.get('unit')
        # if request.POST.get('row'):
        saverecord.row = request.POST.get('row')
        # if request.POST.get('column'):
        saverecord.column = request.POST.get('column')
        # if request.POST.get('pallet'):
        saverecord.pallet = request.POST.get('pallet')
        # if request.POST.get('level'):
        saverecord.level = request.POST.get('level')
        # if request.POST.get('dimension'):
        saverecord.dimension = request.POST.get('dimension')
        # if request.POST.get('weight'):
        saverecord.weight = request.POST.get('weight')
        # if request.POST.get('description'):
        saverecord.description = request.POST.get('description')
        # if request.POST.get('quantity'):
        saverecord.quantity = request.POST.get('quantity')
        # if request.POST.get('make_brand'):
        saverecord.make_brand = request.POST.get('make_brand')
        # if request.POST.get('source'):
        saverecord.source = request.POST.get('source')
        # if request.POST.get('price'):
        saverecord.price = request.POST.get('price')
        # if request.POST.get('product_link'):
        saverecord.product_link = request.POST.get('product_link')
        #saverecord.product_image = myfile
        
        saverecord.save()
        saverecordM.product_pk = Product.objects.get(id=saverecord.id)
        saverecordM.save()
        currentProduct = Product.objects.get(id=saverecord.id)
        if images != None:
            for image in images:
                photo = ProductImages.objects.create(product=currentProduct, image=image )
        
       
        messages.success(request, 'Product added successfully')
        return redirect('uploaderaddproduct')

    if request.user.is_authenticated and request.user.uploader:
        return render(request, 'upload/add.html')
        
    else:
        return redirect( '/accounts/uploadersignin')

    

def details(request, id):
    if request.user.is_authenticated and request.user.uploader:
        product_details = Product.objects.get(id=id)
        return render(request, 'upload/details.html', {"details": product_details})
    else:
        return redirect( '/accounts/uploadersignin')

def edit(request, id):
    if request.method == 'POST' and request.user.is_authenticated :
        Updateproduct = Product.objects.get(id=id)
        images = request.FILES.getlist('product_image')
        fs = FileSystemStorage(location = '/media/productImages')
        for image in images:
            fs.save(image.name, image)
        for image in images:
            photo = ProductImages.objects.create(product= Updateproduct, image=image )
            
                
        form = Productforms(request.POST, instance=Updateproduct)
        print("updating................................")
        #if form.is_valid():
        print('data is valid')
        form.save()
        images = ProductImages.objects.filter(product = Updateproduct)
        messages.success(request, 'Product Updated successfully')
        return render(request, 'upload/edit.html', {"details": Updateproduct, "images" : images})
        

    if request.user.is_authenticated:
        product_details = Product.objects.get(id=id)
        images = ProductImages.objects.filter(product = product_details )
        return render(request, 'upload/edit.html', {"details": product_details, "images" : images})
    else:
        return redirect( '/accounts/uploadersignin')

def delete(request, id):

    if request.user.is_authenticated and request.user.uploader:
        product_details = Product.objects.get(id=id)
        product_details.delete()
        return redirect('uploaderproducts')
    

    else:
        return redirect( '/accounts/uploadersignin')


def imageView(request, id):
    if request.user.is_authenticated and request.user.uploader:
        product = get_object_or_404(Product, id=id)
        images = ProductImages.objects.filter(product = product)
        
        return render(request, 'upload/imageviewer.html', {"product": product, "images" :images} )
    
    
    
    else:
        return redirect( '/accounts/uploadersignin')