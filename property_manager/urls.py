from django.conf.urls import patterns, include, url
from django.contrib import admin
from property_manager import models
from djgeojson.views import GeoJSONLayerView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'property_manager.views.home', name='home'),
    url(r'^add_property$', 'property_manager.views.add_property', name='add_property'),
    url(r'^edit_property/(?P<id>\d+)$', 'property_manager.views.edit_property', name='edit_property'),
    url(r'^property_detail/(?P<id>\d+)$', 'property_manager.views.property_detail', name='property_detail'),

    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=models.Property, properties=('name', 'popupContent',)), name='data'),

    url(r'^login/$', 'property_manager.views.user_login', name="login"),
    url(r'^logout/$', 'property_manager.views.user_logout', name="logout"),
)

# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
