from django.shortcuts import render,redirect
from.models import Category, Product
from django.contrib import messages

def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={'products':products,'categories':categories}
    return render(request,'home.html',context)
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})
def category(request,foo):
    #replace hyphens with spaces
    foo=foo.replace('-',' ')
    #grab category from url
    try:
        #look up category
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        categories = Category.objects.all()
        return render(request,'category.html',{'products':products,'category':category,'categories': categories})
    
    except:
        messages.success(request,'That category does not exist...')
        return redirect('home')