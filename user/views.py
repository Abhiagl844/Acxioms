from django.shortcuts import render, redirect
from .models import User, Order
from vendor.models import Product
from .models import requestItem
from vendor.models import Vendors


def user_signup(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return render(request, "user_signup.html", {"error": "Email already registered"})

        User.objects.create(
            name=name,
            email=email,
            password=password
        )

        return redirect('user_login')

    return render(request, "user_signup.html")


def user_login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email, password=password)
            request.session['user_email'] = user.email
            return redirect('user_portal')
        except User.DoesNotExist:
            return render(request, "user_login.html", {"error": "Invalid Email or Password"})

    return render(request, "user_login.html")


def vendor_category(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    category = request.GET.get("category")

    vend = Vendors.objects.filter(category=category)

    return render(request, "vendor_category.html", {
        "vendors": vend,
        "category": category
    })

def vendor_products_user(request, vendor_id):
    if 'user_email' not in request.session:
        return redirect('user_login')

    products = Product.objects.filter(vendor_id=vendor_id)

    return render(request, "products.html", {
        "products": products,
        "vendor_name": products.first().vendors.name if products else "Vendor"
    })


def user_portal(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    return render(request, "user_portal.html")


def products(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, "products.html", {
        "products": products,
        "vendor_name": category if category else "Vendor"
    })



def cart(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    cart_items = Cart.objects.filter(user_email=request.session['user_email'])

    grand_total = sum(item.total_price for item in cart_items)

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "grand_total": grand_total
    })

def add_to_cart(request, product_id):
    if 'user_email' not in request.session:
        return redirect('user_login')

    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user_email=request.session['user_email'],
        product=product,
        defaults={
            "quantity": 1,
            "total_price": product.price
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.total_price = cart_item.quantity * product.price
        cart_item.save()

    return redirect('cart')


def checkout(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    cart_items = Cart.objects.filter(user_email=request.session['user_email'])
    grand_total = sum(item.total_price for item in cart_items)

    if request.method == "POST":

        request.session['order_name'] = request.POST.get("name")
        request.session['order_phone'] = request.POST.get("phone")
        request.session['order_email'] = request.POST.get("email")
        request.session['order_payment'] = request.POST.get("payment_method")
        request.session['order_address'] = request.POST.get("address")
        request.session['order_state'] = request.POST.get("state")
        request.session['order_city'] = request.POST.get("city")
        request.session['order_pincode'] = request.POST.get("pincode")
        request.session['order_total'] = grand_total

        for item in cart_items:
            Order.objects.create(
                user_email=request.session['user_email'],
                product_name=item.product.name,
                quantity=item.quantity,
                total_price=item.total_price,
                status="Received"
            )

        cart_items.delete()

        return redirect('success')

    return render(request, "checkout.html", {"grand_total": grand_total})




def success(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    return render(request, "success.html")


def order_status(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    orders = Order.objects.filter(user_email=request.session['user_email'])
    return render(request, "order_status.html", {"orders": orders})


def user_logout(request):
    request.session.flush()
    return redirect('home')

def update_cart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    quantity = int(request.POST.get("quantity"))

    item.quantity = quantity
    item.total_price = quantity * item.product.price
    item.save()

    return redirect('cart')


def remove_cart(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return redirect('cart')


def clear_cart(request):
    Cart.objects.filter(user_email=request.session['user_email']).delete()
    return redirect('cart')

def request_item(request):
    if 'user_email' not in request.session:
        return redirect('user_login')

    items = RequestItem.objects.all()

    return render(request, "request_item.html", {
        "request_items": items
    })

def send_request_item(request, item_id):
    if 'user_email' not in request.session:
        return redirect('user_login')

    item = RequestItem.objects.get(id=item_id)

    UserRequest.objects.create(
        user_email=request.session['user_email'],
        item_name=item.name,
        status="Pending"
    )

    return redirect('request_item')