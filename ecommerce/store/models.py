from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	dob = models.DateField()
	phonenumber = models.CharField(max_length=20)
	street = models.CharField(max_length=50)
	suburb = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	postcode = models.PositiveIntegerField()

	def age(self):
		today = date.today()
		age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
		return age
	def __str__(self):
		return self.first_name + " " + self.last_name


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	stock = models.BooleanField(default=True,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	description = models.CharField(max_length=200)
	# digital = models.BooleanField(default=False,null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	street = models.CharField(max_length=200, null=False)
	suburb = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	country = models.CharField(max_length=200, null=False)
	postcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.street + " " + self.suburb + " " + self.city