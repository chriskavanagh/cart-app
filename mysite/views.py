from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserSignInForm

## send_mail('Subject here', 'Here is the message.',
## 'from@example.com', ['to@example.com'],
##  fail_silently=False)



# Create your views here.
@login_required
def user_logout(request):
	'''Logout User.'''
	logout(request)
	return redirect(request.META.get('HTTP_REFERER'))


def my_login(request):
	'''Log User In.'''
	form = UserSignInForm(request.POST)
	if request.method == 'POST':		
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



		
