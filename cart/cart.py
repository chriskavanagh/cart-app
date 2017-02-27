from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
	def __init__(self, request):
		self.request = request
		cart = self.request.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.request.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def __iter__(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			yield item

	def add(self, product, quantity=1, update=False):
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
		if update:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save



	def save(self):
		self.request.session[settings.CART_SESSION_ID] = self.cart
		self.request.session.modified = True
