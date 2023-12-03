from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *
from .forms import ProductSubCatForm

# Create your views here.

def dashboard_view(request):
    products = Product_mst.objects.all()
    return render(request, 'dashboard.html',{'products': products})

def edit_product(request, product_id):
    product = Product_mst.objects.get(pk=product_id)
    form = ProductSubCatForm(request.POST or None, request.FILES or None, instance=product.productsubcat)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')

    return render(request, 'edit_product.html', {'product': product, 'form': form})

# def edit_product(request, product_id):
#     product = Product_mst.objects.get(pk=product_id)
#     if request.method == 'POST':
#         product_subcat = product.productsubcat
#         product_subcat.product_price = request.POST.get('product_price')
#         product_subcat.product_image = request.POST.get('product_image')
#         product_subcat.product_model = request.POST.get('product_model')
#         product_subcat.product_ram = request.POST.get('product_ram')
#         product_subcat.save()
#         product.save()
        
#         return redirect('dashboard_view')

#     return render(request, 'edit_product.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product_mst, product_id=product_id)
    product.delete()
    return redirect('dashboard_view')


def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_model = request.POST.get('product_model')
        product_ram = request.POST.get('product_ram')

        product_mst = Product_mst.objects.create(product_name=product_name)

        product_sub_cat = Product_sub_cat.objects.create(
            product=product_mst,
            product_price=product_price,
            product_model=product_model,
            product_ram=product_ram
        )

        product_image = request.FILES.get('product_image')
        product_sub_cat.product_image = product_image

        # Save both instances
        product_mst.save()
        product_sub_cat.save()

        # Redirect to the dashboard or any other page
        return redirect('dashboard_view')

    return render(request, 'add_product.html')