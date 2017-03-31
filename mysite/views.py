from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .forms import UserSignInForm
from django.contrib.auth import authenticate, login, logout


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
				return redirect(request.META.get('HTTP_REFERER'))
	else:
		HttpResponse("You Are Not Logged In")
		
