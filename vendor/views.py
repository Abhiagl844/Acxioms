from django.shortcuts import render, redirect
from .models import Vendors, Product
from user.models import Order

from django.shortcuts import render, redirect, get_object_or_404



def vendor_signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        category = request.POST.get("category")

        if Vendor.objects.filter(email=email).exists():
            return render(request, "vendor_signup.html", {"error": "Email already registered"})

        Vendor.objects.create(
            name=name,
            email=email,
            password=password,
            category=category
        )

        return redirect('vendor_login')

    return render(request, "vendor_signup.html")



def vendor_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            vendor = Vendor.objects.get(email=email, password=password)
            request.session['vendor_id'] = vendor.id
            return redirect('vendor_dashboard')
        except Vendor.DoesNotExist:
            return render(request, 'vendor_login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'vendor_login.html')




def vendor_dashboard(request):
    if 'vendor_id' not in request.session:
        return redirect('vendor_login')

    vendor = Vendors.objects.get(id=request.session['vendor_id'])

    return render(request, 'vendor_dashboard.html', {
        'vendor': vendor
    })




def delete_product(request, product_id):
    if 'vendor_email' not in request.session:
        return redirect('vendor_login')

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('vendor_dashboard')



def vendor_products(request):
    if 'vendor_email' not in request.session:
        return redirect('vendor_login')

    products = Product.objects.filter(vendor_email=request.session['vendor_email'])
    return render(request, "products.html", {"products": products})


def product_status(request):
    if 'vendor_email' not in request.session:
        return redirect('vendor_login')

    orders = Order.objects.all()
    return render(request, "product_status.html", {"orders": orders})


def update_status(request, order_id):
    if 'vendor_email' not in request.session:
        return redirect('vendor_login')

    order = Order.objects.get(id=order_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        return redirect('product_status')

    return render(request, "update_status.html", {"order": order})

def delete_order(request, order_id):
    Order.objects.get(id=order_id).delete()
    return redirect('product_status')


def vendor_logout(request):
    request.session.flush()
    return redirect('home')

def vendor_items(request):
    if 'vendor_id' not in request.session:
        return redirect('vendor_login')

    products = Product.objects.filter(vendor_id=request.session['vendor_id'])

    return render(request, 'vendor_items.html', {
        'products': products
    })

def add_item(request):
    if 'vendor_id' not in request.session:
        return redirect('vendor_login')

    vendor = Vendor.objects.get(id=request.session['vendor_id'])

    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        image = request.FILES.get('product_image')

        if name and price:
            Product.objects.create(
                vendor=vendor,
                name=name,
                price=price,
                image=image
            )
            return redirect('add_item')

    products = Product.objects.filter(vendor=vendor)

    return render(request, 'add_item.html', {
        'products': products,
        'vendor': vendor
    })
