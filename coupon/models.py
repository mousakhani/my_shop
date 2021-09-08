from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class Coupon(models.Model):
	code = models.CharField(max_length=50, unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	discount = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.code

	def clean(self):
		super(Coupon, self).clean()
		if self.valid_to <= self.valid_from:
			raise ValidationError('"valid to" should bigger than "valid from"')