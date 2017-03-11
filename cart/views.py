from django.shortcuts import render, redirect, get_object_or_404
from coupons.forms import CouponApplyForm
from coupons.models import Coupon
from django.conf import settings
from shop.models import Product
from .forms import ItemAddForm
from decimal import Decimal


def show_cart(request):
	'''display user cart'''
	cart = request.session.get(settings.CART_SESSION_ID, {})
	form = ItemAddForm()
	coupon_form = CouponApplyForm()
	product_ids = cart.keys()
	prod_ids = [int(i) for i in product_ids]
	products = Product.objects.filter(pk__in=prod_ids)

	for product in products:
		cart[str(product.id)]['product'] = product
		cart[str(product.id)]['price'] = Decimal(cart[str(product.id)]['price'])
		cart[str(product.id)]['total_price'] = cart[str(product.id)]['price'] * cart[str(product.id)]['quantity']											   
		q = cart[str(product.id)]['quantity']
		cart[str(product.id)]['update_quantity_form'] = ItemAddForm(initial={'quantity':q,'update': True})

	sub_total = get_cart_total(request, cart)																		 
	disc = get_discount(request, sub_total)	
	cart_total = total_after_disc(request, sub_total, disc)

	cart = cart.values()
	cxt = {'cart': cart,'sub_total':sub_total,'cart_total': cart_total,'coupon_form':coupon_form,'disc':disc}									 
	return render(request, 'cart/cart_detail.html', cxt)


def get_cart_total(request, cart):
	'''get cart total price.'''
	return sum(Decimal(item['price']) * item['quantity'] for item in cart.values())


def get_discount(request, sub_total):
    if request.session.get('coupon_id', None):
        pk = int(request.session['coupon_id'])
        coupon = Coupon.objects.get(pk=pk)
        disc = Decimal(coupon.discount) / Decimal('100') * sub_total
        return disc
    else:
        return None


def total_after_disc(request, sub_total, disc):
	if disc:
		cart_total = sub_total - disc
		return cart_total
	else:
		disc = 0
		cart_total = sub_total - disc
		return cart_total


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
				cart[product_id] = {'product': product.name,
									'quantity': 0,
									'price': str(product.price)}															 					
			if update:
				cart[product_id]['quantity'] = quantity
			else:
				cart[product_id]['quantity'] += quantity
			save_cart(request, cart)
		return redirect('cart:show_cart')


def remove_item(request, pk):
	'''del item from user cart.'''
	product = get_object_or_404(Product, pk=pk)
	product_id = str(product.pk)
	cart = request.session.get(settings.CART_SESSION_ID)
	if product_id in cart:
		del cart[product_id]
		save_cart(request, cart)
	return redirect('cart:show_cart')


def clear_cart(request):
	'''removes all items from cart.'''
	cart = request.session.get(settings.CART_SESSION_ID)
	cart = {}
	request.session[settings.CART_SESSION_ID] = cart
	request.session.modified = True
	#return redirect('cart:show_cart')


def save_cart(request, cart):
	'''save user cart to session.'''
	request.session[settings.CART_SESSION_ID] = cart
	request.session.modified = True


# def get_discount(request):
# 	if request.session['coupon_id']:
# 		pk = int(request.session['coupon_id'])
# 		coupon = Coupon.objects.get(pk=pk)
# 		return Decimal(coupon.discount)
# 	else:
# 		return None


# def show_cart(request):
# 	'''display user cart'''
# 	cart = request.session.get(settings.CART_SESSION_ID, {})
# 	form = ItemAddForm()
# 	coupon_form = CouponApplyForm()
# 	product_ids = cart.keys()
# 	prod_ids = [int(i) for i in product_ids]
# 	products = Product.objects.filter(pk__in=prod_ids)

# 	for product in products:
# 		cart[str(product.id)]['product'] = product
# 		cart[str(product.id)]['price'] = Decimal(cart[str(product.id)]['price'])
# 		cart[str(product.id)]['total_price'] = cart[str(product.id)]['price'] * cart[str(product.id)]['quantity']											   
# 		q = cart[str(product.id)]['quantity']
# 		cart[str(product.id)]['update_quantity_form'] = ItemAddForm(initial={'quantity':q,'update': True})

# 	sub_total = get_cart_total(request, cart)																		 
# 	disc = get_discount(request, sub_total)	
# 	#cart_total = total_after_disc(request, sub_total, disc)
	
# 	# if disc:
# 	# 	disc = disc / Decimal('100') * sub_total
# 	# 	cart_total = sub_total - disc
# 	# else:
# 	# 	disc = None
# 	# 	cart_total = sub_total

# 	cart = cart.values()
# 	cxt = {
# 			'cart': cart,
# 			'sub_total':sub_total,
# 			'cart_total': cart_total,
# 			'coupon_form':coupon_form,
# 			'disc':disc
# 		   }								 
# 	return render(request, 'cart/cart_detail.html', cxt)