from django import forms
from django.contrib.auth.models import User
#from bootstrap_datepicker.widgets import DatePicker
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget




class UserSignInForm(forms.Form):
	username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


## no need to override save method to add email etc.
class SignUpForm(UserCreationForm):
	'''subclass of UserCreationForm.'''
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254,required=True,help_text='Valid Email Required.')							

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class testFormBootstrap3(forms.Form):
	date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
	#todo = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	#date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}))