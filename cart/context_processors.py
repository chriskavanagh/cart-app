from django.conf import settings

def cart_items(request):
	'''returns user cart'''
	cart = request.session.get(settings.CART_SESSION_ID)
	return {'cart': cart}