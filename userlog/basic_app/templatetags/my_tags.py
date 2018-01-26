from django import template

register = template.Library()

@register.filter(name='cutthis')
def cutthis(value, arg):
    """
    This cuts out all values
    """
    return value.replace(arg,'')
