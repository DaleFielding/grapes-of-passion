from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping basket 
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product in the shopping basket"""
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in basket and quantity > 0:
        basket[item_id] = quantity
    elif item_id in basket and quantity <= 0:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""
    basket = request.session.get('basket', {})

    if item_id in basket:
        basket.pop(item_id)

    request.session['basket'] = basket
    return HttpResponse(status=200)