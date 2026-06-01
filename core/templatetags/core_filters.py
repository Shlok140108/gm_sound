from django import template

register = template.Library()


@register.filter(name='split')
def split_filter(value, delimiter='|'):
    """Split a string by delimiter. Usage: {{ "a|b|c"|split:"|" }}"""
    if not value:
        return []
    return str(value).split(delimiter)
