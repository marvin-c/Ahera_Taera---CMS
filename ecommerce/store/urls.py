from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path ('login/', views.login_user, name = 'login'),
    path ('register/', views.register_user, name = 'register'),
	path('logout_user', views.logout_user, name='logout'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('productdetails/<int:product_id>/', views.product_details, name="product_details"),
]