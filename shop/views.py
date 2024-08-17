from django.shortcuts import render,redirect
from.models import Category, Product
from django.contrib import messages
from django.db.models import Q

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
    
def product_search(request):
    query = request.GET.get('search')
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = Product.objects.none()

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search.html', context)