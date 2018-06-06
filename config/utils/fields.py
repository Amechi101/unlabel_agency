from decimal import Decimal
from django.db.models.fields import DecimalField
from django.db.models.fields import CharField

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils import six

from .data import US_STATE_CHOICES, COUNTRY_CHOICES, CONTINENT_CHOICES

@python_2_unicode_compatible
class StateField(CharField):

	description = _("String (up to %(max_length)s)")
	
	def __init__(self, *arg, **kwargs):
		kwargs['max_length'] = 3
		kwargs['blank'] = True
		kwargs['null'] = True
		kwargs['verbose_name'] = 'State/Territories'
		kwargs['help_text'] = 'Required only if in USA'
		kwargs['choices'] = US_STATE_CHOICES
		
		super(StateField, self).__init__(*arg, **kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super(StateField, self).deconstruct()
		if kwargs['max_length'] == 3:
			kwargs.pop('max_length')
		if kwargs['choices'] == US_STATE_CHOICES:
			kwargs.pop('choices')

		return name, path, args, kwargs

	def get_internal_types(self):
		return "CharField"

@python_2_unicode_compatible
class CountryField(CharField):

	description = _("String (up to %(max_length)s)")
	
	def __init__(self, *arg, **kwargs):
		kwargs['max_length'] = 3
		kwargs['verbose_name'] = 'Country'
		kwargs['blank'] = True
		kwargs['null'] = True
		kwargs['choices'] = COUNTRY_CHOICES
		
		super(CountryField, self).__init__(*arg, **kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super(CountryField, self).deconstruct()
		if kwargs['max_length'] == 3:
			kwargs.pop('max_length')
		if kwargs['choices'] == COUNTRY_CHOICES:
			kwargs.pop('choices')

		return name, path, args, kwargs

	def get_internal_types(self):
		return "CharField"

@python_2_unicode_compatible
class ContinentField(CharField):

	description = _("String (up to %(max_length)s)")
	
	def __init__(self, *arg, **kwargs):

		kwargs['max_length'] = 3
		kwargs['blank'] = True
		kwargs['verbose_name'] = 'Continent'
		kwargs['choices'] = CONTINENT_CHOICES
		
		super(ContinentField, self).__init__(*arg, **kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super(ContinentField, self).deconstruct()
		if kwargs['max_length'] == 3:
			kwargs.pop('max_length')
		if kwargs['choices'] == CONTINENT_CHOICES:
			kwargs.pop('choices')

		return name, path, args, kwargs

	def get_internal_types(self):
		return "CharField"


@python_2_unicode_compatible
class CurrencyField(DecimalField):
    """
    A CurrencyField is simply a subclass of DecimalField with a fixed format:
    maxdigits = 30, decimalplaces=10, and defaults to 0.00
    """
    def __init__(self, **kwargs):
        defaults = {
            'max_digits': 30,
            'decimal_places': 2,
            'default': Decimal('0.0')
        }
        defaults.update(kwargs)
        super(CurrencyField, self).__init__(**defaults)	

# https://github.com/django/django/blob/64200c14e0072ba0ffef86da46b2ea82fd1e019a/django/db/models/fields/subclassing.py#L31-L44
class Creator(object):
    """
    A placeholder class that provides a way to set the attribute on the model.
    """
    def __init__(self, field):
        self.field = field

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__[self.field.name]

    def __set__(self, obj, value):
        obj.__dict__[self.field.name] = self.field.to_python(value)

# http://django-oscar.readthedocs.io/en/latest/_modules/oscar/apps/address/abstract_models.html
@python_2_unicode_compatible
class UppercaseCharField(CharField):
    """
    A simple subclass of ``django.db.models.fields.CharField`` that
    restricts all text to be uppercase.

    Defined with the with_metaclass helper so that to_python is called
    https://docs.djangoproject.com/en/1.6/howto/custom-model-fields/#the-subfieldbase-metaclass  # NOQA
    """	

    def contribute_to_class(self, cls, name, **kwargs):
    	super(UppercaseCharField, self).contribute_to_class(cls, name, **kwargs)
    	setattr(cls, self.name, Creator(self))

    def from_db_value(self, value, expression, connection, context):
    	return self.to_python(value)

    def to_python(self, value):
        val = super(UppercaseCharField, self).to_python(value)
        if isinstance(val, six.string_types):
            return val.upper()
        else:
            return val