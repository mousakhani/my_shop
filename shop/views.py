from django.shortcuts import render, get_object_or_404

# Create your views here.
from shop.models import Category, Product


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, '', {
		'category': category,
		'categories': categories,
		'products': products
	})


def product_detail(request, product_id, product_slug):
	product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
	return render(request, '', {'product': product})
