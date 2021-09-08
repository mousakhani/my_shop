from django.contrib import admin

# Register your models here.
from coupon.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
	list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active')
	list_filter = ('active', 'valid_from', 'valid_to', 'discount')
	search_fields = ('code',)
