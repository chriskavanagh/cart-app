from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from shop.models import Product
from .forms import ItemAddForm
from decimal import Decimal


def show_cart(request):
	'''display user cart'''
	cart = request.session.get(settings.CART_SESSION_ID, {})
	form = ItemAddForm()
	product_ids = cart.keys()
	prod_ids = [int(i) for i in product_ids]
	products = Product.objects.filter(pk__in=prod_ids)
	for product in products:
		cart[str(product.id)]['product'] = product
		cart[str(product.id)]['price'] = Decimal(cart[str(product.id)]['price'])

		cart[str(product.id)]['total_price'] = cart[str(product.id)]['price'] * \
						   					   cart[str(product.id)]['quantity']

		q = cart[str(product.id)]['quantity']
		cart[str(product.id)]['update_quantity_form'] = ItemAddForm(initial={'quantity':q,'update': True})
	print cart
																			 																	 
	cart = cart.values()
	cxt = {'cart': cart}
	return render(request, 'cart/cart_detail.html', cxt)


def add_item(request, pk):
	'''add product to user cart'''
	product = get_object_or_404(Product, pk=pk)
	product_id = str(product.pk)
	cart = request.session.get(settings.CART_SESSION_ID, {})
	if request.method == 'POST':
		form = ItemAddForm(request.POST)
		if form.is_valid():
			quantity = form.cleaned_data['quantity']
			update = form.cleaned_data['update']
			if product_id not in cart:
				cart[product_id] = {'product': product.name,'quantity': quantity,'price': str(product.price)}
															 					
			if update:
				cart[product_id]['quantity'] = quantity
			else:
				cart[product_id]['quantity'] += quantity
			save_cart(request, cart)
		return redirect('cart:show_cart')


def remove_item(request, pk):
	"""del item from user cart."""
	product = get_object_or_404(Product, pk=pk)
	product_id = str(product.pk)
	cart = request.session.get(settings.CART_SESSION_ID)
	if product_id in cart:
		del cart[product_id]
		save_cart(request, cart)
	return redirect('shop:product_list')


def save_cart(request, c):
	"""save user cart to session."""
	request.session[settings.CART_SESSION_ID] = c
	request.session.modified = True
