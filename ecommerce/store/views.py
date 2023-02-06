from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django import forms
from .forms import RegisterUserForm    
from django.contrib import messages
from .models import Customer
from datetime import datetime

def store(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		# age = Customer.age(1)
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		# dob = request.user.pk
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		# customer_age = Customer.objects.get(user.pk)
		# age = customer_age.age()
		
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def get_age():
	return request.user.customer.dob

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.success(request, ("Invalid username or password."))
            return render(request, 'store/login.html', {})
    else:
        return render(request, 'store/login.html', {})		


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = request.POST.get('email')
            dob = request.POST.get('dob')
            phonenumber = request.POST.get('phonenumber')
            street = request.POST.get('street')
            suburb = request.POST.get('suburb')
            city = request.POST.get('city')
            country = request.POST.get('country')
            postcode = request.POST.get('postcode')
			# Get the User instance instead of the username string
            user_instance = User.objects.get(username=username)
            Customer.objects.create(user=user_instance,
									first_name=firstname,
                                    last_name=lastname,
                                    email=email,
                                    dob=dob,
                                    phonenumber=phonenumber,
                                    street=street,
                                    suburb=suburb,
                                    city=city,
                                    country=country,
                                    postcode=postcode)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('store')
        else:
            form = RegisterUserForm()
            messages.warning(request, "Error on form... Try again...")
            return render(request, 'store/register.html', {
                'form': form,
            })
    else:
        form = RegisterUserForm()
        return render(request, 'store/register.html', {
            'form': form,
        })

def logout_user(request):
    # messages.success(request, ("You have logged out successfully..."))
    logout(request)
    return redirect('store')