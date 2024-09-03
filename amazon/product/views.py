from django.shortcuts import render,redirect
from product.models import ProductTable


# Create your views here.
def home(request):
    return render(request,'index.html')

def view_product(request):
    data = {}
    products = ProductTable.objects.all()
    data['products'] = products
    return render(request, 'view_product.html', context=data)

def add_product(request):
    if(request.method == 'POST'):
        pname = request.POST['name']
        pprice = request.POST['price']
        pcategory = request.POST['category']
        pavailability = request.POST['availability']
        product = ProductTable.objects.create(name=pname, price=pprice, category=pcategory, availability=pavailability)
        product.save()
        return redirect('/view')
    return render(request, 'add_product.html')

def delete_product(request,product_id):
    product = ProductTable.objects.filter(id=product_id)
    product.delete()
    return redirect('/view')

def update_product(request,product_id):
    data = {}
    product = ProductTable.objects.filter(id=product_id)
    data['product'] = product[0]
    if(request.method == 'POST'):
        pname = request.POST['name']
        pprice = request.POST['price']
        pcategory = request.POST['category']
        pavailability = request.POST['availability']

        ProductTable.objects.update(name=pname, price=pprice, category=pcategory, availability=pavailability)
        return redirect('/view')
    return render(request, 'update_product.html', context=data)


