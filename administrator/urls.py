from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('signup/', views.admin_signup, name='admin_signup'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('maintain-user/', views.maintain_user, name='maintain_user'),
    path('maintain-vendor/', views.maintain_vendor, name='maintain_vendor'),

    path('add-membership/', views.add_membership, name='add_membership'),
    path('update-membership/', views.update_membership, name='update_membership'),

    path('reports/', views.admin_reports, name='admin_reports'),
    path('transactions/', views.admin_transactions, name='admin_transactions'),

    path('logout/', views.admin_logout, name='admin_logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
