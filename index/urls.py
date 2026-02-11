from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart'),

    path('admin-login/', views.admin_login_redirect, name='admin_login_redirect'),
    path('user-login/', views.user_login_redirect, name='user_login_redirect'),
    path('vendor-login/', views.vendor_login_redirect, name='vendor_login_redirect'),

    path('logout/', views.logout, name='logout'),
    path('invalid/', views.invalid_access, name='invalid_access'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
