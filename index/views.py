from django.shortcuts import render, redirect


def home(request):
    if 'admin_email' in request.session:
        return redirect('admin_dashboard')

    if 'user_email' in request.session:
        return redirect('user_portal')

    if 'vendor_email' in request.session:
        return redirect('vendor_dashboard')

    return render(request, "home.html")


def chart(request):
    return render(request, "chart.html")


def admin_login_redirect(request):
    return redirect('admin_login')


def user_login_redirect(request):
    return redirect('user_login')


def vendor_login_redirect(request):
    return redirect('vendor_login')


def logout(request):
    request.session.flush()
    return redirect('home')


def invalid_access(request):
    return render(request, "invalid_access.html")
