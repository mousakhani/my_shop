from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _


class Coupon(models.Model):
	code = models.CharField(verbose_name=_('code'), max_length=50, unique=True)
	valid_from = models.DateTimeField(verbose_name=_('valid_from'))
	valid_to = models.DateTimeField(verbose_name=_('valid_to'))
	discount = models.IntegerField(verbose_name=_('discount'), validators=[MaxValueValidator(100), MinValueValidator(0)])
	active = models.BooleanField(verbose_name=_('active'), default=True)

	def __str__(self):
		return self.code

	def clean(self):
		super(Coupon, self).clean()
		if self.valid_to <= self.valid_from:
			raise ValidationError('"valid to" should bigger than "valid from"')

	class Meta:
		verbose_name = _('Coupon')
		verbose_name_plural = _('Coupons')
