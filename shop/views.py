from django.shortcuts import render, get_object_or_404

# Create your views here.
from cart.forms import CartAddProductForm
from shop.models import Category, Product
from shop.recommender import Recommender


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'shop/products/list.html', {
		'category': category,
		'categories': categories,
		'products': products
	})


def product_detail(request, product_id, product_slug):
	cart_product_form = CartAddProductForm()
	product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
	r = Recommender()
	recommender_products = r.suggest_product_for([product], 4)
	return render(request, 'shop/products/detail.html', {
		'product': product, 'cart_product_form': cart_product_form,
		'recommender_products': recommender_products,
	})
