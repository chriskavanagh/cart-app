from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from cart.forms import ItemAddForm
from django.conf import settings
from .models import Product, Friend, Contact, Friendship
from mysite.forms import UserSignInForm, testFormBootstrap3



# Create your views here.
def product_list(request):
	'''show all products.'''
	#form = UserSignInForm()
	form = testFormBootstrap3()
	products = Product.objects.all()
	#data = request.session.get('coupon_id')
	cxt = {'products': products, 'form':form}
	return render(request, 'shop/products.html', cxt)


def product_detail(request, slug):
	'''show individual product.'''
	product = get_object_or_404(Product, slug=slug, available=True)
	form = ItemAddForm(initial={'quantity': 1, 'update': False})
	user = request.user
	if user.is_authenticated():
		following = user.following.all()
		cxt = {'product': product, 'form': form, 'following':following}
	else:
		cxt = {'product': product, 'form': form}	
	#followers = user.followers.all()
	#people = [f.username for f in friends]
	return render(request, 'shop/item.html', cxt)


def like(request):
	'''like button for product w/AJAX.'''
	if request.method == 'GET':
		pk = request.GET['product_id']
		user = request.user
		product = get_object_or_404(Product, pk=pk)

		if product.user_like.filter(id=user.id).exists():
			product.user_like.remove(user)
		else:
			product.user_like.add(user)
	likes = product.like_count
	return HttpResponse(likes)


# def like_product(request):
# 	'''like button for product.'''
# 	pro_id = None
# 	if request.method == 'GET':
# 		pro_id = request.GET['product_id']

# 	likes = 0
# 	if pro_id:
# 		product = Product.objects.get(pk=int(pro_id))
# 		if product:
# 			likes = product.likes + 1
# 			product.likes = likes
# 			product.save()
# 	return HttpResponse(likes)


# def user_likes(request, slug):
# 	'''MTM relation to user, likes.'''
# 	user = request.user
# 	product = get_object_or_404(Product, slug=slug)
# 	url = product.get_absolute_url()
	
# 	if product.user_like.filter(id=user.id).exists():	# if user in product.user_like.all():
# 		product.user_like.remove(user)		
# 	else:
# 		product.user_like.add(user)
# 	return redirect(url)





