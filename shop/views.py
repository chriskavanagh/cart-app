from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import ItemAddForm
from django.conf import settings
from .models import Product



# Create your views here.
def product_list(request):
	products = Product.objects.all()
	#data = request.session.get(settings.CART_SESSION_ID)
	cxt = {'products': products}
	return render(request, 'shop/products.html', cxt)


def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug, available=True)
	form = ItemAddForm(initial={'quantity': 1, 'update': True})
	cxt = {'product': product, 'form': form}
	return render(request, 'shop/item.html', cxt)