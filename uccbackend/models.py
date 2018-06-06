from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse

from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

from config.utils.fields import StateField, CountryField, UppercaseCharField, CurrencyField
from config.utils.data import SEX_CHOICES, PRODUCT_CATEGORY_CHOICES, STYLE_CHOICES, INDUSTRIES_CHOICES


@python_2_unicode_compatible
class User(AbstractUser):
    is_creator = models.BooleanField(_('Is Creator?'), default=False, help_text=_('Designates whether the user is a creator'))
    
    is_brand = models.BooleanField(_('Is Brand?'), default=False, help_text=_('Designates whether the user is a brand'))

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Brand(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'is_brand': True})

    name = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name=_('Brand Name'))

    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name=_('Brand Description'))

    image = CloudinaryField('Image', null=True, blank=True)

    website = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('Website URL'))

    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('City'))
    
    state = StateField()

    country = CountryField()

    audience = MultiSelectField(max_length=100, choices=SEX_CHOICES, verbose_name=_('Audience'))

    # Admin only
    is_active = models.BooleanField(
        _('Brand Active'),
        default=False,
        help_text=_(
            'Designates whether this brand should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )

    def __str__(self):
        return "{0}".format(self.name)

    # Metadata
    class Meta: 
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_creator': True})

    sex = models.CharField(max_length=15, choices=SEX_CHOICES, null=True, blank=True)

    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    bio = models.TextField(max_length=1000, null=True, blank=True)

    city = models.CharField(max_length=100, null=True, blank=True)
    
    state = StateField()

    country = CountryField()

    image = CloudinaryField('Profile Image', null=True, blank=True)

    instagram_handle = models.CharField(unique=True, max_length=255, null=True, blank=True)
    
    styles = MultiSelectField(max_length=100, choices=STYLE_CHOICES)

    interests = MultiSelectField(max_length=100, choices=PRODUCT_CATEGORY_CHOICES)

    industries = MultiSelectField(max_length=100, choices=INDUSTRIES_CHOICES)

    height = models.PositiveSmallIntegerField(help_text=_('In Inches'), null=True, blank=True)

    chest_bust = models.PositiveSmallIntegerField(help_text=_('In Inches'), null=True, blank=True)

    hips = models.PositiveSmallIntegerField(help_text=_('In Inches'), null=True, blank=True)

    waist = models.PositiveSmallIntegerField(help_text=_('In Inches'), null=True, blank=True)

    is_active = models.BooleanField(_('Is Active?'), default=True, help_text=_('Unselect this instead of deleting data entry.') )

    def __str__(self):
        return self.user.username

    # Metadata
    class Meta: 
        verbose_name = _('Creator')
        verbose_name_plural = _('Creators')


class ShippingAddress(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name='shipping_addresses')

    first_name = models.CharField(_("First name"), max_length=255, blank=True)

    last_name = models.CharField(_("Last name"), max_length=255, blank=True)

    line1 = models.CharField(_("First line of address"), max_length=255, blank=True)
    
    line2 = models.CharField(_("Second line of address"), max_length=255, blank=True)

    city = models.CharField(_("City"), max_length=100, null=True, blank=True)
    
    state = StateField()

    country = CountryField()

    postcode = UppercaseCharField(_("Post/Zip-code"), max_length=64, blank=True)

     # Fields, used for `summary` property definition and hash generation.
     # http://django-oscar.readthedocs.io/en/latest/_modules/oscar/apps/address/abstract_models.html
    base_fields = hash_fields = ['name', 'line1', 'line2', 'city', 'state', 'country', 'postcode']

    def __str__(self):
        return "{0}".format(self.summary)

    # Metadata
    class Meta: 
        verbose_name = _('Shipping Address')
        verbose_name_plural = _('Shipping Addresses')

    # http://django-oscar.readthedocs.io/en/latest/_modules/oscar/apps/address/abstract_models.html

    # Saving

    def clean(self):
        #Strip all whitespace
        for field in ['first_name', 'last_name', 'line1', 'line2', 'city', 'state', 'country', 'postcode']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

    # Properties

    @property
    def summary(self):
        """
        Returns a single string summary of the address,
        separating fields using commas.
        """
        return u", ".join(self.active_address_fields())

    @property
    def name(self):
        return self.join_fields(('first_name', 'last_name'), separator=u" ")

    # Helpers

    def get_field_values(self, fields):
        field_values = []

        for field in fields:

            if field == 'country':
                try:
                    value = self.country
                except exceptions.ObjectDoesNotExist:
                    value = ''
            else:
                value = getattr(self, field)
            field_values.append(value)
        
        return field_values

    def get_address_field_values(self, fields):
        """
        Returns set of field values within the salutation and country.
        """
        field_values = [f.strip() for f in self.get_field_values(fields) if f]
        return field_values

    def generate_hash(self):
        """
        Returns a hash of the address, based on standard set of fields, listed
        out in `hash_fields` property.
        """
        field_values = self.get_address_field_values(self.hash_fields)
        # Python 2 and 3 generates CRC checksum in different ranges, so
        # in order to generate platform-independent value we apply
        # `& 0xffffffff` expression.
        return zlib.crc32(', '.join(field_values).upper().encode('UTF8')) & 0xffffffff

    def join_fields(self, fields, separator=u", "):
        """
        Join a sequence of fields using the specified separator
        """
        field_values = self.get_field_values(fields)
        return separator.join(filter(bool, field_values))

    def active_address_fields(self):
        """
        Returns the non-empty components of the address, but merging the
        title, first_name and last_name into a single line. It uses fields
        listed out in `base_fields` property.
        """
        return self.get_address_field_values(self.base_fields)


@python_2_unicode_compatible
class Product(models.Model):

    PRODUCT_GENDER_CHOICES = (
        ('MALE', _('Men')),
        ('FEMALE', _('Women')),
        ('UNISEX', _('Unisex')),
    )

    CAMPAIGN_CHOICES = (
        ('NONE', _('No Campaign')),
        ('YES', _('Campaign')),
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  null=True, blank=False)
    
    title = models.CharField(max_length=255, null=True, blank=False )

    price = CurrencyField( verbose_name=_('Product Price'), blank=False )

    description = models.TextField(max_length=1000, null=True, blank=False )

    url = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('Product URL'))

    category = MultiSelectField(max_length=100, choices=PRODUCT_CATEGORY_CHOICES)

    image = CloudinaryField('Brand Product Image', null=True, blank=False)

    product_gender_type = models.CharField(max_length=100, choices=PRODUCT_GENDER_CHOICES, null=True, blank=False)

    campaign_type = models.CharField(max_length=100, choices=CAMPAIGN_CHOICES, null=True, blank=False)

    slug = models.SlugField(_('Slug'), max_length=255, unique=False)

    is_active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return "{0}".format(self.title)

    def get_absolute_url(self):
        return reverse('brands:product_detail', kwargs={'product_slug': self.slug, 'pk': self.id})

    # Metadata
    class Meta: 
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

