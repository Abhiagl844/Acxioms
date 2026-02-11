from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('portal/', views.user_portal, name='user_portal'),

    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),

    path('order-status/', views.order_status, name='order_status'),

    path('logout/', views.user_logout, name='user_logout'),
    path('update-cart/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('remove-cart/<int:cart_id>/', views.remove_cart, name='remove_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('request-item/', views.request_item, name='request_item'),
    path('send-request/<int:item_id>/', views.send_request_item, name='send_request_item'),
    path('vendors/', views.vendor_category, name='vendor_category'),
    path('vendor-products/<int:vendor_id>/', views.vendor_products_user, name='vendor_products_user'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

