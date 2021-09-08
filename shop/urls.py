from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('shop/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('shop/<int:product_id>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
