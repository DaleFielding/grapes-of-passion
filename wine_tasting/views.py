from django.shortcuts import render


def wine_tasting(request):

    return render(request, 'wine_tasting/wine_tasting.html')