from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from cart.forms import ItemAddForm
from django.conf import settings
from .models import Product



# Create your views here.
def product_list(request):
	products = Product.objects.all()
	#data = request.session.get('coupon_id')
	cxt = {'products': products}
	return render(request, 'shop/products.html', cxt)


def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug, available=True)
	form = ItemAddForm(initial={'quantity': 1, 'update': False})
	cxt = {'product': product, 'form': form}
	return render(request, 'shop/item.html', cxt)


def like_product(request):
	pro_id = None
	if request.method == 'GET':
		pro_id = request.GET['product_id']

	likes = 0
	if pro_id:
		product = Product.objects.get(pk=int(pro_id))
		if product:
			likes = product.likes + 1
			product.likes = likes
			product.save()
	return HttpResponse(likes)
