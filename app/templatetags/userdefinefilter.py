from django import template

register= template.Library()





def capitalize(value):
    return value.capitalize()

register.filter('cap',capitalize)
