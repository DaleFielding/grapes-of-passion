from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51POC3v2MrHAQw8dWaSIXgSo3g8fRKgB9awgmc7DdiLrZh5WEXhK6f5btCHi3GtptsKSo6y7nQzhpmv2dYSrFuBuo00cO9jzMjH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
