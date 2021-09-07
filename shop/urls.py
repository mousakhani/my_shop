from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
	path('', views.product_list, name='list'),
	path('<slug:category_slug/', views.product_list, name='list_by_category'),
	path('<int:category_id>/<slug:category_slug>/', views.product_detail, name='detail')
]
