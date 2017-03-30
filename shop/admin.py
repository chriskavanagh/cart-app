from django.contrib import admin
from .models import Product, Friendship, Contact

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'description', 'price', 'stock', 'available']

	class Meta:
		model = Product

admin.site.register(Product, ShopAdmin)
admin.site.register(Friendship)
admin.site.register(Contact)