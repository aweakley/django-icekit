from django.conf.urls import include, patterns, url

from .views import iiif_image_api_info, iiif_image_api

urlpatterns = patterns(
    '',
    url(
        r'(?P<identifier>.+)/info.json',
        iiif_image_api_info,
        name='iiif_image_api_info',
    ),
    url(
        r'(?P<identifier>[^/]+)/(?P<region>[^/]+)/(?P<size>[^/]+)'
        r'/(?P<rotation>[^/]+)/(?P<quality>[^.]+).(?P<output_format>.+)',
        iiif_image_api,
        name='iiif_image_api',
    ),
)