from django.db import models
from django.utils.html import escape, mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from cloudinary.models import CloudinaryField

from multiselectfield import MultiSelectField

from config.utils.data import SEX_CHOICES

from decimal import Decimal


# @python_2_unicode_compatible
# class ProductCategory(models.Model):
#     name = models.CharField(max_length=30)
#     color = models.CharField(max_length=7, default='#007bff')

#     def get_html_badge(self):
#         name = escape(self.name)
#         color = escape(self.color)
#         html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
#         return mark_safe(html)

#     def __str__(self):
#         return self.name

#     # Metadata
#     class Meta: 
#         verbose_name = _('Product Category')
#         verbose_name_plural = _('Product Categories')


# @python_2_unicode_compatible
# class ProductSizeOptions(models.Model):

#     SIZE_ATTRIBUTE_CHOICES = (
#         ("IN", _("Inches")),
#         ("US", _("US")),
#     )

#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  null=True, blank=False)
    
#     name = models.CharField(max_length=255, null=True, blank=False)
    
#     size_name = models.CharField(max_length=255, null=True, blank=False)

#     size_attribute = models.CharField(max_length=100, blank=True, null=True, choices=SIZE_ATTRIBUTE_CHOICES)

#     size_code = models.CharField(max_length=100, blank=True, null=True, choices=PRODUCT_SIZE_CODE_CHOICES)

#     def __str__(self):
#         return "{0}".format(self.name)

#     # Metadata
#     class Meta: 
#         verbose_name = _('Product Size Option')
#         verbose_name_plural = _('Product Size Options')


@python_2_unicode_compatible
class Product(models.Model):

    PRODUCT_GENDER_CHOICES = (
        ('MALE', _('Men')),
        ('FEMALE', _('Women')),
        ('UNISEX', _('Unisex')),
    )

    PRODUCT_GENDER_CHOICES = (
        ('MALE', _('Men')),
        ('FEMALE', _('Women')),
        ('UNISEX', _('Unisex')),
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  null=True, blank=False)
    
    title = models.CharField(max_length=255, null=True, blank=False )

    price = CurrencyField( verbose_name=_('Product Price'), blank=False )

    description = models.TextField(max_length=1000, null=True, blank=False )

    url = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('Product URL'))

    # category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=False)

    image = CloudinaryField('Brand Product Image', null=True, blank=False)

    product_type = models.CharField(max_length=15, choices=PRODUCT_DISCOUNT_CHOICES, null=True, blank=True)

    slug = models.SlugField(_('Slug'), max_length=255, unique=False)

    is_active = models.BooleanField(_('Is Active?'), default=True, help_text=_('Unselect this instead of deleting data entry.') )

    def __str__(self):
        return "{0}".format(self.title)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'product_slug': self.slug, 'pk': self.id})

    # Metadata
    class Meta: 
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


# @python_2_unicode_compatible
# class ProductSelected(models.Model):

#     product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    
#     creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name='interested_product')

#     date_selected = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

#     def __str__(self):
#         return "{0}, {1}".format(self.product, self.creator)

#     # Metadata
#     class Meta: 
#         verbose_name = _('Selected Product ')
#         verbose_name_plural = _('Selected Products')


# @python_2_unicode_compatible
# class ProductReview(models.Model):

#     product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)

#     creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name='reviewed_product')

#     review_image_1 = CloudinaryField('Review Image', null=True, blank=True)

#     review_image_2 = CloudinaryField('Review Image', null=True, blank=True)

#     review_image_3 = CloudinaryField('Review Image', null=True, blank=True)

#     review_image_4 = CloudinaryField('Review Image', null=True, blank=True)

#     review_image_5 = CloudinaryField('Review Image', null=True, blank=True)
    
#     video = CloudinaryField('Review Video', resource_type="video", null=True, blank=True)

#     summary = models.TextField(max_length=1000, null=True, blank=True)

#     date_completed = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#     purchase_product = models.BooleanField(_('Purchase Product'), default=False)

#     def __str__(self):
#         return "{0}, {1}".format(self.product, self.creator)

#     # Metadata
#     class Meta: 
#         verbose_name = _('Product Review')
#         verbose_name_plural = _('Product Reviews')



