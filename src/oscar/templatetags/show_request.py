from django import template
from ..apps.basket import my_middleware

register = template.Library()

@register.simple_tag
def request_made():
    my_middleware.my_list.append("end of request")
    return my_middleware.my_list[0:-1]

@register.simple_tag
def request_made_len():
    return len(my_middleware.my_list[0:-1])
