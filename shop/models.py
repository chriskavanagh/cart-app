from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = AutoSlugField(populate_from='name', unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default = 0)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		 return reverse('shop:product_detail', args=[self.slug])