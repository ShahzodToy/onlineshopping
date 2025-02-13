from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path(_('cart/'),include('cart.urls')),
    path(_('orders/'),include('orders.urls')),
    path(_('coupons/'),include('coupons.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('',include('product.urls')),
    
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
