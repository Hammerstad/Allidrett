from django import template

register = template.Library()


@register.filter
def should_be_disabled(value):
    return '0 ledige plasser' in value
