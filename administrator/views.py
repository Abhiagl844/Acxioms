from django.shortcuts import render, redirect
from .models import Admin, Membership
from user.models import User, Order
from vendor.models import Vendors


def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        try:
            admin = Admin.objects.get(email=email, password=password)
            request.session['admin_email'] = admin.email
            return redirect('admin_dashboard')
        except:
            return render(request, "admin_login.html", {"error": "Invalid Credentials"})

    return render(request, "admin_login.html")


def admin_signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not Admin.objects.filter(email=email).exists():
            Admin.objects.create(name=name, email=email, password=password)
            return redirect('admin_login')

    return render(request, "admin_signup.html")


def admin_dashboard(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    return render(request, "admin.html")


def maintain_user(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    users = User.objects.all()
    return render(request, "maintain_user.html", {"users": users})


def maintain_vendor(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    vendors = Vendor.objects.all()
    return render(request, "maintain_vendor.html", {"vendors": vendors})


def add_membership(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    if request.method == "POST":
        membership_number = request.POST.get("membership_number")
        user_email = request.POST.get("user_email")
        duration = request.POST.get("duration")

        Membership.objects.create(
            membership_number=membership_number,
            user_email=user_email,
            duration=duration
        )

        return redirect('admin_dashboard')

    return render(request, "add_membership.html")


def update_membership(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    if request.method == "POST":
        membership_number = request.POST.get("membership_number")
        action = request.POST.get("action")

        membership = Membership.objects.get(membership_number=membership_number)

        if action == "extend":
            membership.duration = '6'
            membership.save()

        if action == "cancel":
            membership.active = False
            membership.save()

        return redirect('admin_dashboard')

    return render(request, "update_membership.html")


def admin_reports(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    orders = Order.objects.all()
    return render(request, "admin_reports.html", {"orders": orders})


def admin_transactions(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')

    orders = Order.objects.all()
    return render(request, "admin_transactions.html", {"orders": orders})


def admin_logout(request):
    request.session.flush()
    return redirect('home')
