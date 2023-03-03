from django import template

register = template.Library()

@register.filter
def split_by_comma(string):
    return string.split(',')
