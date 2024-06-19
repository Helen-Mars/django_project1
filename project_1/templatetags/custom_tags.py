from django import template


register = template.Library()


@register.simple_tag
def uppercase(value):
    """Converts a string into all uppercase."""
    return value.upper()
