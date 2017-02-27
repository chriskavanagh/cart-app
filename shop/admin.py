from django.contrib import admin
from .models import Product

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'description', 'price', 'stock', 'available']

	class Meta:
		model = Product

admin.site.register(Product, ShopAdmin)