from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def creator_discount(value):

	discount = value * Decimal(0.70)
	return int(round(discount))