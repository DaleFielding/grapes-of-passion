from django import forms
from .models import WineTastingProduct


class WineTastingForm(forms.Form):
    experience = forms.ChoiceField(
        required=True,
    )
    contact_number = forms.CharField(
        max_length=15,
        required=True,
    )
    special_requirements = forms.CharField(
        required=False
    )
    date = forms.CharField(
        required=True,
    )
    quantity = forms.IntegerField(
        min_value=1,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['experience'].choices = [('', '-Experiences-')] + [
            (product.id, product.product_name) for product in WineTastingProduct.objects.all()
        ]
        for field in self.fields:
            self.fields[field].label = False
