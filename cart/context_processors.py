from django.conf import settings
from shop.models import Product


def cart_items(request):
	'''returns user cart'''
	cart = request.session.get(settings.CART_SESSION_ID, {})
	cart_length = len(cart)
	return {'cart_item_count': cart_length}


def show_cart_items(request):
	cart = request.session.get(settings.CART_SESSION_ID, {})
	cart_items = cart.values()
	return {'cart_items':cart_items}


def user_likes(request):
	user = request.user
	likes = user.product_likes.all()
	prod_names = [str(p.name) for p in likes]
	return {'likes': prod_names}