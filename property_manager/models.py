from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static
from django.core.urlresolvers import reverse
from django.utils.text import Truncator



POPUP = '''
<div class="media">
  <div class="media-left">
    <a href="{}">
      <img class="media-object" src="{}">
    </a>
  </div>
  <div class="media-body">
    <h4 class="media-heading">{}</h4>
    {}
  </div>
</div>
'''

class Property(models.Model):
    name = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
    )

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True
    )

    last_modified_date = models.DateTimeField(
        verbose_name=_('Last modified date'),
        auto_now=True
    )

    description = models.TextField(
        verbose_name=_('Description'),
        default='',
        blank=True,
        null=True
    )

    photo = models.ImageField(
        verbose_name=_("photo"),
        upload_to='photos/',
        default='/static/img/empty.gif'
    )

    def get_absolute_url(self):
        return reverse('property_detail', args=[self.pk])

    @property
    def popupContent(self):
        return POPUP.format(
          self.get_absolute_url(),
          self.photo.url,
          self.name,
          Truncator(self.description).words(40, html=True, truncate='...')
        )

    geom = models.PointField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
