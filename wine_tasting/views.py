from django.shortcuts import render, redirect
from .models import WineTastingProduct
from .forms import WineTastingForm
import json


def wine_tasting(request):
    if request.method == 'POST':
        form = WineTastingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('wine_tasting')  
    else:
        form = WineTastingForm()

    wine_tastings = WineTastingProduct.objects.all()
    dates_dict = {str(product.id): product.dates.split(',') for product in wine_tastings}

    return render(request, 'wine_tasting/wine_tasting.html', {
        'WineTastingProducts': wine_tastings,
        'form': form,
        'dates_json': json.dumps(dates_dict)
    })
