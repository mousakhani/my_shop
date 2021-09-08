import redis
from django.conf import settings
from shop.models import Product

# connect to redis
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class Recommender(object):
	def get_product_key(self, id):
		# نام مجموعه هایی که در ردیس استفاده می شود از این گرفته می شود
		return f'Product:{id} : purchased_with'

	def products_bought(self, products):
		product_ids = [product.id for product in products]
		for product_id in product_ids:
			for with_id in product_ids:
				# get the other products with each other product
				if product_id != with_id:
					# increment score for product purchased together
					"""
					در مجموعه ی self.get_product_key(product_id)(که مرتب شده است) مقدار with_id به اندازه ی یک(1) واحد افزایش می یابد
					"""
					r.zincrby(self.get_product_key(product_id), 1, with_id)

	def suggest_product_for(self, products, max_result=6):
		product_ids = [p.id for p in products]
		if len(products) == 1:
			# only 1 product
			# zrange
			"""
			از مجموعه ی مرتب شده ی name(آرگمان اول) از start تا end مقادیر را بر میگرداند. در صورتی که end مقدار 1- 
			بگیرد. به این معنی است که تا انتها برگرداند.
			"""
			suggestions = r.zrange(self.get_product_key(product_ids[0]), 0, -1, desc=True)[:max_result]
		else:
			# generate a temporary key
			flat_ids = ''.join([str[id] for id in product_ids])
			tmp_key = f'tmp_{flat_ids}'
			# multiple products, combine scores of all products
			# store the resulting sorted set in a temporary key
			keys = [self.get_product_key(id) for id in product_ids]
			r.zunionstore(tmp_key, keys)
			# remove ids for the products the recommendation is for
			# حذف لیست داده شده از مجموعه ی name(ارگمان اول)
			r.zrem(tmp_key, *product_ids)
			# get the product_ids by their score, descendant sort
			suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_result]
			# remove the temporary key
			r.delete(tmp_key)
		suggested_product_ids = [int(id) for id in suggestions]
		# get suggested products and sort by order of appearance
		suggested_products = list(Product.objects.filter(id__in=suggested_product_ids))
		suggested_products.sort(key=lambda x: suggested_product_ids.index(x.id))
		return suggested_products

	def clear_purchases(self):
		for id in Product.objects.values_list('id', flat=True):
			r.delete(self.get_product_key(id))
