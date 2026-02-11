from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.vendor_signup, name='vendor_signup'),
    path('login/', views.vendor_login, name='vendor_login'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/', views.vendor_products, name='vendor_products'),

    path('product-status/', views.product_status, name='product_status'),
    path('update-status/<int:order_id>/', views.update_status, name='update_status'),

    path('logout/', views.vendor_logout, name='vendor_logout'),
    path('items/', views.vendor_items, name='vendor_items'),
    path('add-item/', views.add_item, name='add_item'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
