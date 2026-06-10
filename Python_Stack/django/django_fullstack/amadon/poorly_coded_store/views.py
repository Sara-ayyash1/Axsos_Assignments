from django.shortcuts import render,redirect
from .models import Order, Product
import bcrypt

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def buy(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id)
            current_charge = product.price * quantity
        except Product.DoesNotExist:
            return redirect('/')

        request.session['last_charge'] = float(current_charge)
        
        request.session['total_items'] = request.session.get('total_items', 0) + quantity
        request.session['total_spent'] = request.session.get('total_spent', 0) + float(current_charge)
        
        return redirect('/checkout/')
        
    return redirect('/')

def checkout(request):
    if 'last_charge' not in request.session:
        return redirect('/')
        
    return render(request, "store/checkout.html")

def clear_session(request):
    request.session.flush()
    return redirect('/')