# shops/views.py

from django.shortcuts import render, redirect
from .forms import ShopRegistrationForm

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_success')  # Create a success URL or template
    else:
        form = ShopRegistrationForm()
    return render(request, 'shops/register_shop.html', {'form': form})
