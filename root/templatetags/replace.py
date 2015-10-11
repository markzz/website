from django import template

register = template.Library()


def presentable(value):
    return value.replace('-', ' ')

register.filter('presentable', presentable)