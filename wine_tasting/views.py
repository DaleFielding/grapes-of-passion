from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WineTastingProduct, WineTastingBooking
from .forms import WineTastingForm
from django.contrib.auth.decorators import login_required
import json

@login_required
def wine_tasting(request):
    if request.method == 'POST':
        form = WineTastingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            wine_tasting_product = WineTastingProduct.objects.get(id=booking.wine_tasting_product.id)
            booking.total_price = wine_tasting_product.price * booking.number_of_people
            
            booking.save()
            messages.success(request, 'Booking was successful, please pay on the day you arrive.')
            return redirect('wine_tasting')
    else:
        form_data = request.session.pop('form_data', None)
        form = WineTastingForm(form_data)

    wine_tastings = WineTastingProduct.objects.all()
    dates_dict = {str(product.id): product.dates.split(',') for product in wine_tastings}
    experiences_info = {
        str(product.id): {
            'name': product.product_name,
            'min_quantity': 2 if 'couple' in product.product_name.lower() else 3,
            'max_quantity': 2 if 'couple' in product.product_name.lower() else 12
        } for product in wine_tastings
    }
    price = wine_tastings.first().price if wine_tastings else 0

    return render(request, 'wine_tasting/wine_tasting.html', {
        'WineTastingProducts': wine_tastings,
        'form': form,
        'dates_json': json.dumps(dates_dict),
        'experiences_info_json': json.dumps(experiences_info),
        'price': price
    })
