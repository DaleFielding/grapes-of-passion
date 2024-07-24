from django import forms
from .models import WineTastingBooking, WineTastingProduct

class WineTastingForm(forms.ModelForm):
    class Meta:
        model = WineTastingBooking
        fields = ['wine_tasting_product', 'contact_number', 'special_requirements', 'selected_date', 'number_of_people']
        labels = {
            'wine_tasting_product': '',
            'contact_number': '',
            'special_requirements': '',
            'selected_date': '',
            'number_of_people': ''
        }

    wine_tasting_product = forms.ChoiceField(required=True)
    contact_number = forms.CharField(max_length=15, required=True)
    special_requirements = forms.CharField(required=False)
    selected_date = forms.DateTimeField(required=True)
    number_of_people = forms.IntegerField(min_value=1, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wine_tasting_product'].choices = [('', '-Experiences-')] + [
            (product.id, product.product_name) for product in WineTastingProduct.objects.all()
        ]
    
    def clean_wine_tasting_product(self):
        product_id = self.cleaned_data['wine_tasting_product']
        try:
            product = WineTastingProduct.objects.get(id=product_id)
        except WineTastingProduct.DoesNotExist:
            raise forms.ValidationError("Invalid wine tasting product selected.")
        return product