from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
