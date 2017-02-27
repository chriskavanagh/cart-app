from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



class ItemAddForm(forms.Form):
	 quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
	 update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput(attrs={'class': 'form-control'}))

	 # def __init__(self, *args, **kwargs):
	 # 	super(ItemAddForm, self).__init__(*args, **kwargs)
	 # 	self.helper = FormHelper()
	 # 	self.helper.form_method = 'post'
	 # 	self.helper.form_class = 'form-inline'
	 # 	self.helper.field_template = 'bootstrap3/layout/inline_field.html'

	 # 	self.helper.layout = Layout(
	 # 		'quantity', 'update',
	 # 		ButtonHolder(Submit('submit', 'Update', css_class='btn btn-primary btn-sm')
	 # 			)
	 # 		)
