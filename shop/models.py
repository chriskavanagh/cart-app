from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail
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

	def save(self, *args, **kwargs):
		item = super(Product, self).save(*args, **kwargs)
		message = "{} was created at {}".format(self.name, self.created.strftime('%Y-%m-%d, %I:%M %p'))
		send_mail('Product Created',message,'from@example.com',['ckava3@gmail.com'],fail_silently=False)
  		return item

	def __unicode__(self):
		return self.name

	@property
	def like_count(self):
		return self.user_like.count()

	def get_absolute_url(self):
		 return reverse('shop:product_detail', args=[self.slug])


## from Django 1.0 Website Development p 192
class Friendship(models.Model):
	from_friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="friend_set")
	to_friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="to_friend_set")

	class Meta:
		unique_together = (('to_friend', 'from_friend'), )

	def __unicode__(self):
		return "{} is following {}".format(self.from_friend.username, self.to_friend.username)


## from https://www.youtube.com/watch?v=nwpLCa79DUw&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=56
class Friend(models.Model):
	users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="friends")
	current_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner")

	@classmethod
	def make_friend(cls, current_user, new_friend):		
		friend = cls.objects.get_or_create(current_user=current_user)[0]
		friend.users.add(new_friend)

	def __unicode__(self):
		return self.current_user.username


## from Django By Example
class Contact(models.Model):
	user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="rel_from_set")
	user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="rel_to_set")
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __unicode__(self):
		return "{} follows {}".format(self.user_from, self.user_to)


User.add_to_class("following",
				   models.ManyToManyField("self",
				   						   through=Contact,
				   						   related_name="followers",
				   						   symmetrical=False))


