from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models




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
	user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,
									   related_name='product_likes')		   

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return self.name

	@property
	def like_count(self):
		return self.user_like.count()

	def get_absolute_url(self):
		 return reverse('shop:product_detail', args=[self.slug])