from django.test import TestCase, Client
from .models import Customer, Product, Order
import datetime
from django.contrib.auth.models import User
from .forms import RegisterUserForm

# Create your tests here.
class BasicTest(TestCase):

     # 1. test Customer table if saving customer data
    def test_Customer(self):
        customer = Customer()
        customer.first_name = "Marvin"
        customer.last_name = "Coronel"
        customer.email = "marvin@gmail.com"
        customer.dob = "1986-02-14"
        customer.phonenumber = "02101145784"
        customer.street = "18 Don Buck Road"
        customer.suburb = "Massey"
        customer.city = "Auckland"
        customer.country = "New Zealand"
        customer.postcode = "1421"
        customer.save()

        record = Customer.objects.get(pk=1)
         # check if the mock data is actually saved and equal to assert.
        self.assertEqual(record, customer) 

    # 2. test Product table if saving product data
    def test_Product(self):
        product = Product()
        product.name = "Head & Shoulders"
        product.price = 4.99
        product.stock = True
        product.image = "shampoo.png"
        product.description = "Shampoo and Conditioner"
        product.save()

        record = Product.objects.get(pk=1)
         # check if the mock data is actually saved and equal to assert.
        self.assertEqual(record, product) 

    # 3. test Order table if saving customer order data
    def test_Order(self):
        order = Order()
        order.date_ordered = datetime.datetime.now()
        order.complete = True
        order.transactionid = datetime.datetime.now().timestamp()
        order.save()

        record = Order.objects.get(pk=1)
         # check if the mock data is actually saved and equal to assert.
        self.assertEqual(record, order) 

    # 4. test if user Mcjev can login
    def test_Login(self):
        user = User.objects.create(username='mcjev')
        user.set_password('Welcome123')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')

# 5. Test if non admin user can access admin page of ecommerce webapp
class NonAdminAccessTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.non_admin_user = User.objects.create_user(
            username='nonadmin', password='secret')
        self.client.login(username='nonadmin', password='secret')
        
    def test_non_admin_access(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)


class RegisterUserFormTestCase(TestCase):
    # 6. Test form if data is valid.
    def test_valid_form(self):
        form_data = {
            'username': 'marvinc',
            'email': 'mcjev@gmail.com',
            'first_name': 'Marvin',
            'last_name': 'Coronel',
            'dob': '1984-04-20',
            'phonenumber': '0210514457',
            'street': '74 Henderson Road',
            'suburb': 'Henderson',
            'city': 'Auckland',
            'country': 'New Zealand',
            'postcode': 4124,
            'password1': 'Sunshine123',
            'password2': 'Sunshine123',
        }
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        print(form.errors)

    # 7. Test form if data is invalid.
    def test_invalid_form(self):
        form_data = {
            'username': 'user1',
            'email': 'invalidemail',
            'first_name': 'Jake',
            'last_name': 'Relon',
            'dob': '1994-02-01',
            'phonenumber': '021544873',
            'street': '14 Quay Street',
            'suburb': 'Northcote',
            'city': 'Hamilton',
            'country': 'New Zealand',
            'postcode': 4115,
            'password1': 'password123',
            'password2': 'password12',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())        