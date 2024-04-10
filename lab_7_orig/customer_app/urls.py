# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('list/', views.CustomerList.as_view(), name='customer-list'),
    path('edit/<int:customer_id>/', views.CustomerEdit.as_view(), name='customer-edit'),
    path('order_list/', views.OrderList.as_view(), name='order-list'),
    path('order_edit/<int:order_id>/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_edit/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_delete/<int:order_id>/', views.OrderDelete.as_view(), name='order-delete'),
    path('contact_edit/<int:contact_id>/', views.ContactEdit.as_view(), name='contact-edit'),
    path('contact_edit/', views.ContactEdit.as_view(), name='contact-edit')

]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
