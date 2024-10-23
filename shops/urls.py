# shops/urls.py

from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView
from .views import register_shop

urlpatterns = [
    path('register/', register_shop, name='register_shop'),
    path('success/', TemplateView.as_view(template_name='shops/success.html'), name='shop_success'),  # Create a success template
]
