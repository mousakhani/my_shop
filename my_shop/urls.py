"""my_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# توجه شود. در ادرسی دهی، url ها باید از جزء ها به کل ها مرتب شوند.
# مثلا در کد زیر اگر خط مربوط به اپ shop را بالاتر از خطوط مربوط به اپ های cart و orders
# قرار دهیم، هیچ گاه cart و orders مسیریابی نخواهند شد. چون قبل از اینکه نوبت به آنها برسد
# در اپ shop یا مسیر پیدا شده و یا اگر پیدا نشده مقدار 404 برگشت داده می شود.
# به عبارت دیگر وقتی مسیر وارد include شود دیگر از آن خارج نمی شود، مگر مسیر پیدا شده یا 404 شود.
urlpatterns = i18n_patterns(
	path('admin/', admin.site.urls),
	path('rosetta/', include('rosetta.urls')),
	path('orders/', include('orders.urls')),
	path('cart/', include('cart.urls')),
	path('coupon/', include('coupon.urls')),
	path('', include('shop.urls')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

