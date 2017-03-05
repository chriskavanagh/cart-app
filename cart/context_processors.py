from django.conf import settings

def cart_items(request):
	'''returns user cart'''
	cart = request.session.get(settings.CART_SESSION_ID, {})
	cart_length = len(cart)
	return {'cart_item_count': cart_length}