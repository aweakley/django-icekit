import re

from django.core import exceptions
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from fluent_contents.models import ContentItem

# This will likely have to be tended as GMaps will change their
#  Share URL format over time.
# See tests.py
SHARE_URL_PATTERN = r'place\/((?P<name>.+)\/)?\@(?P<loc>.+)\/'


@python_2_unicode_compatible
class MapItem(ContentItem):
    """
    Embeds a Google Map inside an iframe from the Share URL.

    Rather than store the width/height in the DB, update the template
    used or override with CSS.
    """
    share_url = models.URLField(
        help_text='Share URL sourced from Google Maps. '
                  'See https://support.google.com/maps/answer/144361?hl=en',
        verbose_name='Share URL',
        max_length=500,
    )

    place_name = 'Unknown'
    loc = '0, 0'

    class Meta:
        verbose_name = 'Google Map'

    def clean(self, *args, **kwargs):
        self.parse_share_url()
        super(MapItem, self).clean(*args, **kwargs)

    def parse_share_url(self):
        """Search the Share URL for place name and lat/lon coordinates."""
        regex = re.compile(SHARE_URL_PATTERN)
        result = regex.search(str(self.share_url))
        if getattr(result, 'groupdict'):
            self.place_name = result.groupdict()['name']
            self.loc = result.groupdict()['loc']
        else:
            raise exceptions.ValidationError('Could not parse map Share URL')

    def __str__(self):
        if self.place_name == 'Unknown':
            self.parse_share_url()
        return '%s @%s' % (self.place_name, self.loc)

    def save(self, *args, **kwargs):
        self.parse_share_url()

        return super(MapItem, self).save(*args, **kwargs)