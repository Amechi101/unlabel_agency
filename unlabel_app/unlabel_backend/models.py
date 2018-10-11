from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse

from .abstract_models import TimeModel

from multiselectfield import MultiSelectField

from cloudinary.models import CloudinaryField

from config.utils.data import SERVICES_CHOICES


@python_2_unicode_compatible
class Project(TimeModel):
    
    title = models.CharField(max_length=255, null=True, blank=False)

    client_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Client Name') )

    cover_image = CloudinaryField('Cover Image', null=True, blank=True)

    description = models.TextField(max_length=1000, null=True, blank=True )

    services = MultiSelectField(max_length=100, choices=SERVICES_CHOICES )

    slug = models.SlugField(_('Slug'), max_length=255, unique=True, blank=True)

    is_active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return "{0}: {1}".format(self.title, self.client_name)

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        
        self.full_clean()
        
        super(Project, self).save(*args, **kwargs)

    # Metadata
    class Meta: 
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


@python_2_unicode_compatible
class ProjectImage(models.Model):

	project = models.ForeignKey(Project, on_delete=models.CASCADE,  null=True, blank=True, verbose_name=_('Project'), related_name='images')
    
	image = CloudinaryField('Image', null=True, blank=True)

	def __str__(self):
		return "Image of {0}".format(self.project)

	# Metadata
	class Meta: 
		verbose_name = _('Project Image')
		verbose_name_plural = _('Project Images')

