from django import forms
from django.utils.translation import ugettext as _


class CouponApplyForm(forms.Form):
	code = forms.CharField(label=_('code'))
