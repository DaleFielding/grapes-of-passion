from django import forms
from .models import Product, Category


# ---------- PRODUCT FORM: ADMIN ----------
class ProductForm(forms.ModelForm):
    """
    Django Form for the Product model to set category choices and custom styling.
    """
    class Meta:
        model = Product
        fields = '__all__'

    # Sets the category field choices to the list with the friendly names
    # Applies custom css class and custom label for region state
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['region_state'].label = "Region/State"
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'