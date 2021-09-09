from django.db import models

# Create your models here.
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _


class Category(TranslatableModel):
	translations = TranslatedFields(
		name=models.CharField(max_length=200, db_index=True),
		slug=models.SlugField(max_length=200, unique=True)
	)

	# django-parler does not supported this code
	class Meta:
		verbose_name_plural = _('Categories')

	# 	ordering = ('name',)

	def __str__(self):
		return self.translations.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=(self.slug,))


class Product(TranslatableModel):
	translations = TranslatedFields(
		name=models.CharField(max_length=200, db_index=True),
		slug=models.SlugField(max_length=200, db_index=True),
		description=models.TextField(blank=True),

	)
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# django-parler does not supported this codes
	# class Meta:
	# 	ordering = ('name',)
	# 	index_together = (('id', 'slug'),)

	def __str__(self):
		return self.translations.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=(self.id, self.slug))
