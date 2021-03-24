from django.template import Library

register = Library()


@register.simple_tag
def get_tag_list():
    pass


@register.simple_tag
def get_category_list():
    pass


@register.simple_tag
def get_friend_link_list():
    pass
