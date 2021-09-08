from django import forms
from django.utils.translation import ugettext_lazy as _
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label=_('quantity'),choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	override = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=False)
