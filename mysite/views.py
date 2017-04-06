from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserSignInForm, SignUpForm

## send_mail('Subject here', 'Here is the message.',
## 'from@example.com', ['to@example.com'],
##  fail_silently=False)



## no longer used. allauth is used instead
def signup(request):
	'''standard uer registration form.'''
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('shop:product_list')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})


## no longer used. allauth is used instead
@login_required
def user_logout(request):
	'''standard user logout.'''
	logout(request)
	return redirect(request.META.get('HTTP_REFERER'))
	

## no longer used. allauth is used instead
def user_login(request):
	'''standard user login.'''
	if request.method == 'POST':
		form = UserSignInForm(request.POST)		
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None and user.is_active:
				login(request, user)
				messages.success(request, 'Welcome %s.' % request.user.username)
				return redirect(request.META.get('HTTP_REFERER'))
			else:
				messages.warning(request, 'Please Provide A Valid Username Or Password')
				return redirect(request.META.get('HTTP_REFERER'))
	else:
		raise Http404



		
