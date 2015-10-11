from django import template
from django.utils.html import strip_tags

register = template.Library()


def presentable(value):
    return value.replace('-', ' ')

register.filter('presentable', presentable)

