from django.shortcuts import render, redirect
from .models import WineTastingProduct
from .forms import WineTastingForm
import json


def wine_tasting(request):
    if request.method == 'POST':
        form = WineTastingForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('wine_tasting')  
    else:
        form = WineTastingForm()

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
