from django import template


# Custom template filter calculates subtotal by multiplying price and quantity
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
